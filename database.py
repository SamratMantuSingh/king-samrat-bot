import sqlite3
import psycopg2
from psycopg2.extras import RealDictCursor
from contextlib import contextmanager
import config

class DatabaseManager:
    def __init__(self):
        self.use_postgres = config.DATABASE_URL.startswith("postgres")
    
    @contextmanager
    def get_connection(self):
        conn = None
        try:
            if self.use_postgres:
                conn = psycopg2.connect(config.DATABASE_URL, cursor_factory=RealDictCursor)
            else:
                conn = sqlite3.connect(config.DATABASE_URL.replace("sqlite:///", ""))
                conn.row_factory = sqlite3.Row
            yield conn
            conn.commit()
        finally:
            if conn:
                conn.close()
    
    def initialize_tables(self):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            
            # Notification Queue Table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS notification_queue (
                    id SERIAL PRIMARY KEY,
                    priority INTEGER NOT NULL,
                    section TEXT NOT NULL,
                    message TEXT NOT NULL,
                    timestamp TIMESTAMP NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            
            # Trade History Table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS trade_history (
                    id SERIAL PRIMARY KEY,
                    timestamp TIMESTAMP NOT NULL,
                    section TEXT NOT NULL,
                    symbol TEXT NOT NULL,
                    exchange TEXT,
                    direction TEXT,
                    entry_price REAL,
                    sl_price REAL,
                    tp1_price REAL,
                    tp2_price REAL,
                    tp3_price REAL,
                    status TEXT DEFAULT 'PENDING',
                    tp1_hit BOOLEAN DEFAULT FALSE,
                    tp2_hit BOOLEAN DEFAULT FALSE,
                    tp3_hit BOOLEAN DEFAULT FALSE,
                    sl_hit BOOLEAN DEFAULT FALSE,
                    profit_loss REAL,
                    funding_prev REAL,
                    funding_current REAL,
                    funding_next REAL
                )
            """)
            
            # Daily Stats Table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS daily_stats (
                    date DATE PRIMARY KEY,
                    signals_sent INTEGER DEFAULT 0,
                    tp1_hits INTEGER DEFAULT 0,
                    tp2_hits INTEGER DEFAULT 0,
                    tp3_hits INTEGER DEFAULT 0,
                    sl_hits INTEGER DEFAULT 0,
                    pending_trades INTEGER DEFAULT 0,
                    win_rate REAL DEFAULT 0,
                    total_profit REAL DEFAULT 0,
                    avg_rr REAL DEFAULT 0,
                    funding_earned REAL DEFAULT 0
                )
            """)
            
            # Funding Rates History
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS funding_rates (
                    id SERIAL PRIMARY KEY,
                    timestamp TIMESTAMP NOT NULL,
                    symbol TEXT NOT NULL,
                    exchange TEXT NOT NULL,
                    previous_rate REAL,
                    current_rate REAL,
                    next_rate REAL,
                    interval TEXT
                )
            """)
    
    def add_notification(self, priority, section, message, timestamp):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO notification_queue (priority, section, message, timestamp)
                VALUES (%s, %s, %s, %s)
            """, (priority, section, message, timestamp))
    
    def get_notifications(self, limit=10):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT id, message FROM notification_queue 
                ORDER BY priority DESC, created_at ASC 
                LIMIT %s
            """, (limit,))
            return cursor.fetchall()
    
    def delete_notification(self, notification_id):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM notification_queue WHERE id = %s", (notification_id,))
    
    def add_trade(self, trade_data):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO trade_history (
                    timestamp, section, symbol, exchange, direction,
                    entry_price, sl_price, tp1_price, tp2_price, tp3_price,
                    funding_prev, funding_current, funding_next
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                RETURNING id
            """, (
                trade_data['timestamp'], trade_data['section'], trade_data['symbol'],
                trade_data.get('exchange'), trade_data.get('direction'),
                trade_data.get('entry'), trade_data.get('sl'), trade_data.get('tp1'),
                trade_data.get('tp2'), trade_data.get('tp3'),
                trade_data.get('funding_prev'), trade_data.get('funding_current'),
                trade_data.get('funding_next')
            ))
            return cursor.fetchone()['id']
    
    def get_daily_stats(self, date):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT * FROM daily_stats WHERE date = %s
            """, (date,))
            return cursor.fetchone()
    
    def update_daily_stats(self, date, stats):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO daily_stats (
                    date, signals_sent, tp1_hits, tp2_hits, tp3_hits,
                    sl_hits, pending_trades, win_rate, total_profit, avg_rr, funding_earned
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                ON CONFLICT (date) DO UPDATE SET
                    signals_sent = EXCLUDED.signals_sent,
                    tp1_hits = EXCLUDED.tp1_hits,
                    tp2_hits = EXCLUDED.tp2_hits,
                    tp3_hits = EXCLUDED.tp3_hits,
                    sl_hits = EXCLUDED.sl_hits,
                    pending_trades = EXCLUDED.pending_trades,
                    win_rate = EXCLUDED.win_rate,
                    total_profit = EXCLUDED.total_profit,
                    avg_rr = EXCLUDED.avg_rr,
                    funding_earned = EXCLUDED.funding_earned
            """, (
                date, stats['signals_sent'], stats['tp1_hits'], stats['tp2_hits'],
                stats['tp3_hits'], stats['sl_hits'], stats['pending_trades'],
                stats['win_rate'], stats['total_profit'], stats['avg_rr'],
                stats.get('funding_earned', 0)
            ))
