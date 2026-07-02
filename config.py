import os
from datetime import timezone, timedelta

# Telegram Configuration
TELEGRAM_BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN", "")
TELEGRAM_CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID", "")

# Redis Configuration (Render provides this)
REDIS_URL = os.environ.get("REDIS_URL", "redis://localhost:6379")

# Database Configuration (Render PostgreSQL)
DATABASE_URL = os.environ.get("DATABASE_URL", "sqlite:///king_samrat.db")

# Timezone
IST = timezone(timedelta(hours=5, minutes=30))

# Priority Levels
PRIORITY_HIGHEST = 3  # ⭐⭐⭐
PRIORITY_HIGH = 2      # ⭐⭐
PRIORITY_MEDIUM = 1    # ⭐
PRIORITY_LOW = 0       # No stars

# Refresh Intervals (seconds)
REFRESH_INTERVAL = 600  # 10 minutes
REPORT_INTERVAL = 3600  # 1 hour

# Telegram Rate Limiting
TELEGRAM_DELAY = 1.5  # seconds between messages

# Portfolio Configuration
DEFAULT_PORTFOLIO_VALUE = 10000  # $10,000

# Exchange List
SUPPORTED_EXCHANGES = ["Binance", "Bybit", "OKX", "Bitget"]
