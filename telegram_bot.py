import aiohttp
import asyncio
import config

class TelegramBot:
    def __init__(self):
        self.bot_token = config.TELEGRAM_BOT_TOKEN
        self.chat_id = config.TELEGRAM_CHAT_ID
        self.base_url = f"https://api.telegram.org/bot{self.bot_token}"
        self.sent_messages = set()  # Prevent duplicates
    
    async def send_message(self, message, parse_mode="HTML"):
        """Send message to Telegram with duplicate prevention"""
        # Create a hash of the message to prevent duplicates
        msg_hash = hash(message)
        if msg_hash in self.sent_messages:
            return False
        
        url = f"{self.base_url}/sendMessage"
        payload = {
            "chat_id": self.chat_id,
            "text": message,
            "parse_mode": parse_mode,
            "disable_web_page_preview": True
        }
        
        try:
            async with aiohttp.ClientSession() as session:
                async with session.post(url, json=payload) as response:
                    if response.status == 200:
                        self.sent_messages.add(msg_hash)
                        # Keep only last 1000 messages in memory
                        if len(self.sent_messages) > 1000:
                            self.sent_messages = set(list(self.sent_messages)[-1000:])
                        return True
                    elif response.status == 429:
                        # Rate limited
                        retry_after = (await response.json()).get('parameters', {}).get('retry_after', 5)
                        await asyncio.sleep(retry_after)
                        return await self.send_message(message, parse_mode)
                    else:
                        print(f"Telegram API Error: {response.status}")
                        return False
        except Exception as e:
            print(f"Error sending Telegram message: {e}")
            return False
    
    async def send_with_delay(self, messages):
        """Send multiple messages with delay to prevent rate limiting"""
        for msg in messages:
            success = await self.send_message(msg)
            if success:
                await asyncio.sleep(config.TELEGRAM_DELAY)
