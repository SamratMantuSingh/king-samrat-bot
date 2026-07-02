import asyncio
import os
from datetime import datetime, timedelta
import schedule
from flask import Flask
from database import DatabaseManager
from telegram_bot import TelegramBot
from notifications import NotificationFormatter
from reports import ReportGenerator
import config

# Flask app for keeping Render awake
app = Flask(__name__)

@app.route('/')
def home():
    return "👑 King Samrat Singh Bot - Institutional Grade Crypto Signals"

@app.route('/health')
def health():
    return {"status": "healthy", "timestamp": datetime.now(config.IST).isoformat()}

async def main():
    """Main bot execution"""
    print("👑 Initializing King Samrat Singh Bot...")
    
    # Initialize components
    db = DatabaseManager()
    db.initialize_tables()
    bot = TelegramBot()
    formatter = NotificationFormatter()
    reports = ReportGenerator(db)
    
    # Send test notification
    test_data = {
        'symbol': 'BTC', 'stars': '⭐⭐⭐', 'price': '68450',
        'exchanges': 'Binance, Bybit', 'portfolio': 10000, 'size': 5,
        'direction': '🟢 LONG BIAS', 'prob_up': '85', 'prob_down': '15',
        'f_prev': '+0.01%', 'f_curr': '+0.03%', 'f_next': '+0.05%',
        'old_int': '8h', 'new_int': '1h', 'next_fund_time': '42m',
        'vol_level': '🔴 Extreme', 'vol_mult': '🔴 4.2x', 'trend': '🟢 Strong Bull',
        'oi': '🟠 +28%', 'sentiment': '🔴 E.Greed', 'entry': '67800',
        'hold_time': '4-8 Hours', 'sl': '67200', 'tp': '69500',
        'alpha': 'Exchange forcing rapid sentiment reset. Drop leverage to 2x.'
    }
    
    test_message = formatter.funding_interval_shift(test_data)
    await bot.send_message(test_message)
    
    print("✅ Bot initialized successfully. Running dispatcher...")
    
    # Main dispatcher loop
    while True:
        try:
            # Get notifications from queue
            notifications = db.get_notifications(limit=10)
            
            if notifications:
                for notif in notifications:
                    await bot.send_message(notif['message'])
                    db.delete_notification(notif['id'])
                    await asyncio.sleep(config.TELEGRAM_DELAY)
            
            await asyncio.sleep(5)
            
        except Exception as e:
            print(f"Error in main loop: {e}")
            await asyncio.sleep(10)

def run_scheduler():
    """Run scheduled tasks (reports)"""
    schedule.every().day.at("09:00").do(lambda: print("Daily report scheduled"))
    schedule.every().sunday.at("09:00").do(lambda: print("Weekly report scheduled"))
    schedule.every().day.at("09:00").do(lambda: print("Monthly check scheduled"))
    
    while True:
        schedule.run_pending()
        asyncio.run(main())

if __name__ == "__main__":
    # Run Flask and bot concurrently
    import threading
    
    def run_flask():
        app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
    
    # Start Flask in a separate thread
    flask_thread = threading.Thread(target=run_flask, daemon=True)
    flask_thread.start()
    
    # Run main bot
    asyncio.run(main())
