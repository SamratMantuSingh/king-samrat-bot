# 👑 King Samrat Singh - Institutional Grade Crypto Bot

## Features
- 15 Complete Notification Sections
- Star Priority System (⭐⭐⭐ Highest, ⭐⭐ High, ⭐ Medium)
- Daily/Weekly/Monthly Reports
- Zero Missed Notifications
- Multi-Exchange Support (Binance, Bybit, OKX, Bitget)
- Complete Funding Rate Analysis
- Entry/SL/TP Levels with Hold Duration
- Portfolio Value Tracking

## Deployment on Render

### Step 1: Create Render Account
1. Go to https://render.com
2. Sign up for free account

### Step 2: Create PostgreSQL Database
1. Click "New" → "PostgreSQL"
2. Name: `king-samrat-db`
3. Region: Choose closest to you
4. Click "Create Database"
5. Copy the **Internal Database URL**

### Step 3: Create Redis Database
1. Click "New" → "Redis"
2. Name: `king-samrat-redis`
3. Click "Create Database"
4. Copy the **Redis URL**

### Step 4: Create Web Service
1. Click "New" → "Web Service"
2. Connect your GitHub repository
3. Configuration:
   - Name: `king-samrat-bot`
   - Region: Same as databases
   - Branch: `main`
   - Root Directory: `/`
   - Runtime: `Python 3`
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `python main.py`
   - Instance Type: Free

### Step 5: Add Environment Variables
In the "Environment" section, add:
