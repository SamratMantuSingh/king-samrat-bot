from datetime import datetime
import config

class NotificationFormatter:
    """All 15 notification sections with complete formatting"""
    
    @staticmethod
    def get_timestamp():
        return datetime.now(config.IST).strftime("%H:%M IST, %d %b %Y")
    
    def funding_interval_shift(self, data):
        """Section 1: Funding Rate Interval Change"""
        return f"""👑 <b>King Samrat Singh</b>
━━━━━━━━━━━━━━━━━━━━━━
🔄 <b>FUNDING INTERVAL SHIFT</b>
━━━━━━━━━━━━━━━━━━━━━━
🪙 <b>{data['symbol']}</b> {data['stars']} | 💰 <code>${data['price']}</code>
💼 Portfolio: ${data.get('portfolio', 10000):,} | Size: {data.get('size', 5)}% (${int(data.get('portfolio', 10000) * data.get('size', 5) / 100)})
🏦 {data['exchanges']}
📈 Direction: {data['direction']} | 📊 Prob: 📈 {data['prob_up']}% | 📉 {data['prob_down']}%
━━━━━━━━━━━━━━━━━━━━━━
📊 <b>Funding:</b> Prev: {data['f_prev']} | Curr: {data['f_curr']} | Next: {data['f_next']}
⏱️ Shift: {data['old_int']} ➡️ {data['new_int']} | ⏰ Next Funding: {data['next_fund_time']}
🌡️ Vol: {data['vol_level']} | 📊 Vol$: {data['vol_mult']} | 📈 Trend: {data['trend']}
💰 OI: {data['oi']} | 🧠 Sent: {data['sentiment']}
━━━━━━━━━━━━━━━━━━━━━━
🎯 <b>Trade Setup:</b>
🎯 Best Entry: ${data['entry']} | ⏳ Hold Duration: {data['hold_time']}
🛑 SL: ${data['sl']} | TP: ${data['tp']}
🧠 <i>{data['alpha']}</i>
🕒 <i>{self.get_timestamp()}</i>"""

    def funding_sign_change(self, data):
        """Section 2: Funding Rate Sign Change"""
        return f"""👑 <b>King Samrat Singh</b>
━━━━━━━━━━━━━━━━━━━━━━
📉 <b>FUNDING SIGN FLIP</b>
━━━━━━━━━━━━━━━━━━━━━━
🪙 <b>{data['symbol']}</b> {data['stars']} | 💰 <code>${data['price']}</code>
💼 Portfolio: ${data.get('portfolio', 10000):,} | Size: {data.get('size', 10)}%
🏦 {data['exchanges']}
📈 Direction: {data['direction']} | 📊 Prob: 📈 {data['prob_up']}% | 📉 {data['prob_down']}%
━━━━━━━━━━━━━━━━━━━━━━
📊 <b>Funding:</b> Prev: {data['f_prev']} | Curr: {data['f_curr']} | Next: {data['f_next']}
⏰ Next Funding: {data['next_fund_time']}
🌡️ Vol: {data['vol_level']} | 📊 Vol$: {data['vol_mult']} | 📈 Trend: {data['trend']}
💰 OI: {data['oi']} | 📐 RSI: {data['rsi']} | 🧠 Sent: {data['sentiment']}
🐋 Whale: {data['whale']}
━━━━━━━━━━━━━━━━━━━━━━
🎯 <b>Trade Setup:</b>
🎯 Best Entry: ${data['entry']} | ⏳ Hold Duration: {data['hold_time']}
🛑 SL: ${data['sl']} | TP: ${data['tp']}
🧠 <i>{data['alpha']}</i>
🕒 <i>{self.get_timestamp()}</i>"""

    def token_unlock(self, data):
        """Section 3: Token Unlock (30 Days Prior)"""
        return f"""👑 <b>King Samrat Singh</b>
━━━━━━━━━━━━━━━━━━━━━━
🔓 <b>VESTING CLIFF: 30 DAYS</b>
━━━━━━━━━━━━━━━━━━━━━━
🪙 <b>{data['symbol']}</b> {data['stars']} | 💰 <code>${data['price']}</code>
💼 Portfolio: ${data.get('portfolio', 10000):,} | Action: {data.get('action', 'Reduce by 20%')}
📈 Direction: {data['direction']} | 📊 Prob: 📈 {data['prob_up']}% | 📉 {data['prob_down']}%
━━━━━━━━━━━━━━━━━━━━━━
📊 <b>Funding:</b> Prev: {data.get('f_prev', 'N/A')} | Curr: {data.get('f_curr', 'N/A')} | Next: {data.get('f_next', 'N/A')}
📦 {data['amount']} ({data['value']}) | {data['percent']} Supply
👤 {data['unlock_type']} | 📉 Pressure: {data['pressure']}
📈 Trend: {data['trend']} | 🧠 Sent: {data['sentiment']}
🐋 Whale: {data['whale']} | 💎 Smart: {data['smart']}
📊 Hist: {data['hist_impact']}
━━━━━━━━━━━━━━━━━━━━━━
🎯 <b>Trade Setup:</b>
🎯 Best Entry: ${data['entry']} | ⏳ Hold Duration: {data['hold_time']}
🛑 SL: ${data['sl']} | TP: ${data['tp']}
🧠 <i>{data['alpha']}</i>
🕒 <i>{self.get_timestamp()}</i>"""

    def ath_atl_breach(self, data):
        """Section 4: ATH/ATL Breach"""
        return f"""👑 <b>King Samrat Singh</b>
━━━━━━━━━━━━━━━━━━━━━━
{data['icon']} <b>{data['type']} BREACHED</b>
━━━━━━━━━━━━━━━━━━━━━━
🪙 <b>{data['symbol']}</b> {data['stars']} | 💰 <code>${data['price']}</code>
💼 Portfolio: ${data.get('portfolio', 10000):,} | Size: {data.get('size', 15)}%
🏦 {data['exchanges']}
📈 Direction: {data['direction']} | 📊 Prob: 📈 {data['prob_up']}% | 📉 {data['prob_down']}%
━━━━━━━━━━━━━━━━━━━━━━
📊 <b>Funding:</b> Prev: {data['f_prev']} | Curr: {data['f_curr']} | Next: {data['f_next']}
{data['icon']} {data['type']} | Prev: ${data['prev_price']}
🌡️ Vol: {data['vol_level']} | 📊 Vol$: {data['vol_mult']}
📈 Trend: {data['trend']} | 📐 RSI: {data['rsi']} | ⚡ Mom: {data['momentum']}
💰 OI: {data['oi']} | 🧠 Sent: {data['sentiment']} | 🐋 Whale: {data['whale']}
━━━━━━━━━━━━━━━━━━━━━━
🎯 <b>Trade Setup:</b>
🎯 Best Entry: ${data['entry']} | ⏳ Hold Duration: {data['hold_time']}
🛑 SL: ${data['sl']} | TP: ${data['tp']}
🧠 <i>{data['alpha']}</i>
🕒 <i>{self.get_timestamp()}</i>"""

    def manipulation_detection(self, data):
        """Section 5: Manipulation Detection"""
        return f"""👑 <b>King Samrat Singh</b>
━━━━━━━━━━━━━━━━━━━━━━
🚨 <b>MANIPULATION DETECTED</b>
━━━━━━━━━━━━━━━━━━━━━━
🪙 <b>{data['symbol']}</b> {data['stars']} | 💰 <code>${data['price']}</code>
💼 Portfolio: ${data.get('portfolio', 10000):,} | Action: {data.get('action', 'EXIT ALL')}
📈 Direction: {data['direction']} | 📊 Prob: 📈 {data['prob_up']}% | 📉 {data['prob_down']}%
━━━━━━━━━━━━━━━━━━━━━━
📊 <b>Funding:</b> Prev: {data['f_prev']} | Curr: {data['f_curr']} | Next: {data['f_next']}
⚠️ {data['manipulation_type']}
📊 Fake Bid: {data['fake_bid']} | 💰 Pump: {data['pump']}
📊 Vol$: {data['vol_mult']} | 🌡️ Vol: {data['vol_level']}
📈 Trend: {data['trend']} | 🧠 Sent: {data['sentiment']}
🐋 Whale: {data['whale']} | 📉 OB: {data['ob_fake']}
━━━━━━━━━━━━━━━━━━━━━━
🎯 <b>Trade Setup:</b>
🎯 Best Entry: {data['entry']} | ⏳ Hold Duration: {data['hold_time']}
🛑 SL: {data['sl']} | TP: ${data['tp']}
🧠 <i>{data['alpha']}</i>
🕒 <i>{self.get_timestamp()}</i>"""

    def official_notification(self, data):
        """Section 6: Official Exchange Notification"""
        return f"""👑 <b>King Samrat Singh</b>
━━━━━━━━━━━━━━━━━━━━━━
📢 <b>OFFICIAL EXCHANGE ALERT</b>
━━━━━━━━━━━━━━━━━━━━━━
🏦 {data['exchange']} | 📌 {data['alert_type']}
🪙 <b>{data['symbol']}</b> {data['stars']} | 💰 {data['price_label']}: <code>${data['price']}</code>
💼 Portfolio: ${data.get('portfolio', 10000):,} | Size: {data.get('size', 2)}%
📈 Direction: {data['direction']} | 📊 Prob: 📈 {data['prob_up']}% | 📉 {data['prob_down']}%
━━━━━━━━━━━━━━━━━━━━━━
📊 <b>Funding:</b> Prev: {data.get('f_prev', 'N/A')} | Curr: {data.get('f_curr', 'N/A')} | Next: {data.get('f_next', 'N/A')}
⏳ Starts: {data['start_time']} | 📊 Hist Pump: {data['hist_pump']}
📈 Phase: {data['phase']} | 💎 Smart: {data['smart']} | 🛡️ Risk: {data['risk']}
━━━━━━━━━━━━━━━━━━━━━━
🎯 <b>Trade Setup:</b>
🎯 Best Entry: ${data['entry']} | ⏳ Hold Duration: {data['hold_time']}
🛑 SL: ${data['sl']} | TP: ${data['tp']}
🧠 <i>{data['alpha']}</i>
🕒 <i>{self.get_timestamp()}</i>"""

    def rumor_tracking(self, data):
        """Section 7: Major Rumor Tracking"""
        return f"""👑 <b>King Samrat Singh</b>
━━━━━━━━━━━━━━━━━━━━━━
🗣️ <b>HIGH-SIGNAL RUMOR</b>
━━━━━━━━━━━━━━━━━━━━━━
🪙 <b>{data['symbol']}</b> {data['stars']} | 💰 <code>${data['price']}</code>
💼 Portfolio: ${data.get('portfolio', 10000):,} | Size: {data.get('size', 3)}%
📈 Direction: {data['direction']} | 📊 Prob: 📈 {data['prob_up']}% | 📉 {data['prob_down']}%
━━━━━━━━━━━━━━━━━━━━━━
📊 <b>Funding:</b> Prev: {data.get('f_prev', 'N/A')} | Curr: {data.get('f_curr', 'N/A')} | Next: {data.get('f_next', 'N/A')}
📌 {data['topic']} | 🎯 Cred: {data['credibility']}
🐋 Whale: {data['whale']} | 💎 Smart: {data['smart']}
📊 Sent: {data['sentiment']} | 📈 Trend: {data['trend']} | 📊 On-chain: {data['onchain']}
🛡️ Risk: {data['risk']}
━━━━━━━━━━━━━━━━━━━━━━
🎯 <b>Trade Setup:</b>
🎯 Best Entry: ${data['entry']} | ⏳ Hold Duration: {data['hold_time']}
🛑 SL: ${data['sl']} | TP: ${data['tp']}
🧠 <i>{data['alpha']}</i>
🕒 <i>{self.get_timestamp()}</i>"""

    def spotlight_event(self, data):
        """Section 8: Spotlights & Major Events"""
        return f"""👑 <b>King Samrat Singh</b>
━━━━━━━━━━━━━━━━━━━━━━
🌟 <b>FREE YIELD EVENT</b>
━━━━━━━━━━━━━━━━━━━━━━
🏦 {data['exchange']}
🪙 {data['token']} {data['stars']} | {data['event_type']}
💼 Portfolio: ${data.get('portfolio', 10000):,} | Action: {data['action']}
📈 Direction: {data['direction']} | 📊 Prob: 📈 {data['prob_up']}%
━━━━━━━━━━━━━━━━━━━━━━
📊 <b>Funding:</b> N/A (Spot Event)
💰 APY: {data['apy']} | ⏳ Lock: {data['lock_period']} | 🛡️ Risk: {data['risk']}
📊 Cap Eff: {data['cap_eff']} | 💎 Smart: {data['smart']}
━━━━━━━━━━━━━━━━━━━━━━
🎯 <b>Trade Setup:</b>
🎯 Best Entry: {data['entry']} | ⏳ Hold Duration: {data['hold_time']}
🛑 SL: {data['sl']} | TP: {data['tp']}
🧠 <i>{data['alpha']}</i>
🕒 <i>{self.get_timestamp()}</i>"""

    def extreme_metrics(self, data):
        """Section 9: Extreme Metrics (75%+ Threshold)"""
        return f"""👑 <b>King Samrat Singh</b>
━━━━━━━━━━━━━━━━━━━━━━
🌡️ <b>EXTREME CROWD METRIC</b>
━━━━━━━━━━━━━━━━━━━━━━
🪙 <b>{data['symbol']}</b> {data['stars']} | 💰 <code>${data['price']}</code>
💼 Portfolio: ${data.get('portfolio', 10000):,} | Size: {data.get('size', 5)}%
🏦 {data['exchanges']}
📈 Direction: {data['direction']} | 📊 Prob: 📈 {data['prob_up']}% | 📉 {data['prob_down']}%
━━━━━━━━━━━━━━━━━━━━━━
📊 <b>Funding:</b> Prev: {data['f_prev']} | Curr: {data['f_curr']} | Next: {data['f_next']}
📊 L/S Ratio: {data['ls_ratio']} | 📉 Liq Risk: {data['liq_risk']}
💰 OI: {data['oi']} | 📈 Signal: {data['signal']}
🐋 Whale: {data['whale']} | 💎 Smart: {data['smart']}
━━━━━━━━━━━━━━━━━━━━━━
🎯 <b>Trade Setup:</b>
🎯 Best Entry: ${data['entry']} | ⏳ Hold Duration: {data['hold_time']}
🛑 SL: ${data['sl']} | TP: ${data['tp']}
🧠 <i>{data['alpha']}</i>
🕒 <i>{self.get_timestamp()}</i>"""

    def liquidation_heatmap(self, data):
        """Section 10: Liquidation Heatmap"""
        return f"""👑 <b>King Samrat Singh</b>
━━━━━━━━━━━━━━━━━━━━━━
🗺️ <b>LIQUIDATION MAGNET ACTIVE</b>
━━━━━━━━━━━━━━━━━━━━━━
🪙 <b>{data['symbol']}</b> {data['stars']} | 💰 <code>${data['price']}</code>
💼 Portfolio: ${data.get('portfolio', 10000):,} | Size: {data.get('size', 8)}%
🏦 {data['exchanges']}
📈 Direction: {data['direction']} | 📊 Prob: 📈 {data['prob_up']}% | 📉 {data['prob_down']}%
━━━━━━━━━━━━━━━━━━━━━━
📊 <b>Funding:</b> Prev: {data['f_prev']} | Curr: {data['f_curr']} | Next: {data['f_next']}
💰 Target: <code>${data['target']}</code> | 💧 Liq: ${data['liq_vol']}M
📏 Distance: {data['distance']} | 🧲 Magnet: {data['magnet']}
📈 Trend: {data['trend']} | 🐋 Whale: {data['whale']} | 💎 Smart: {data['smart']}
━━━━━━━━━━━━━━━━━━━━━━
🎯 <b>Trade Setup:</b>
🎯 Best Entry: ${data['entry']} | ⏳ Hold Duration: {data['hold_time']}
🛑 SL: ${data['sl']} | TP: ${data['tp']}
🧠 <i>{data['alpha']}</i>
🕒 <i>{self.get_timestamp()}</i>"""

    def high_prob_long(self, data):
        """Section 11: High-Probability Long Setup"""
        return f"""👑 <b>King Samrat Singh</b>
━━━━━━━━━━━━━━━━━━━━━━
🟢 <b>HIGH-PROB LONG SETUP</b>
━━━━━━━━━━━━━━━━━━━━━━
🪙 <b>{data['symbol']}</b> {data['stars']} | 💰 <code>${data['price']}</code>
💼 Portfolio: ${data.get('portfolio', 10000):,} | Size: {data.get('size', 5)}%
🏦 {data['exchanges']}
📈 Direction:  LONG | 📊 Prob: 📈 {data['prob_up']}% | 📉 {data['prob_down']}%
━━━━━━━━━━━━━━━━━━━━━━
📊 <b>Funding:</b> Prev: {data['f_prev']} | Curr: {data['f_curr']} | Next: {data['f_next']}
📊 Win Rate: {data['win_rate']}% | 🎯 R:R: {data['rr']} | 📈 Percentile: {data['percentile']}
💵 Cumulative Paid: {data['cumulative']} | ⏰ Next Funding: {data['next_fund_time']}
🌡️ Vol: {data['vol_level']} | 📊 Vol$: {data['vol_mult']} | 📈 Trend: {data['trend']}
💰 OI: {data['oi']} | 📐 RSI: {data['rsi']} | 🧠 Sent: {data['sentiment']}
🐋 Whale: {data['whale']} | 💎 Smart: {data['smart']}
━━━━━━━━━━━━━━━━━━━━━━
🎯 <b>Trade Setup:</b>
🎯 Best Entry: ${data['entry']} | ⏳ Hold Duration: {data['hold_time']}
🛑 SL: ${data['sl']} (-{data['sl_pct']}%) | ✅ TP1: ${data['tp1']} | ✅ TP2: ${data['tp2']} | ✅ TP3: ${data['tp3']}
📊 Leverage: {data['leverage']} | 🛡️ Risk: {data['risk']}
🧠 <i>{data['alpha']}</i>
🕒 <i>{self.get_timestamp()}</i>"""

    def high_prob_short(self, data):
        """Section 12: High-Probability Short Setup"""
        return f"""👑 <b>King Samrat Singh</b>
━━━━━━━━━━━━━━━━━━━━━━
🔴 <b>HIGH-PROB SHORT SETUP</b>
━━━━━━━━━━━━━━━━━━━━━━
🪙 <b>{data['symbol']}</b> {data['stars']} | 💰 <code>${data['price']}</code>
💼 Portfolio: ${data.get('portfolio', 10000):,} | Size: {data.get('size', 3)}%
🏦 {data['exchanges']}
📈 Direction: 🔴 SHORT | 📊 Prob:  {data['prob_up']}% | 📉 {data['prob_down']}%
━━━━━━━━━━━━━━━━━━━━━━
📊 <b>Funding:</b> Prev: {data['f_prev']} | Curr: {data['f_curr']} | Next: {data['f_next']}
📊 Win Rate: {data['win_rate']}% | 🎯 R:R: {data['rr']} | 📈 Percentile: {data['percentile']}
💵 Cumulative Paid: {data['cumulative']} | ⏰ Next Funding: {data['next_fund_time']}
🌡️ Vol: {data['vol_level']} | 📊 Vol$: {data['vol_mult']} | 📈 Trend: {data['trend']}
💰 OI: {data['oi']} | 📐 RSI: {data['rsi']} | 🧠 Sent: {data['sentiment']}
🐋 Whale: {data['whale']} | 💎 Smart: {data['smart']}
━━━━━━━━━━━━━━━━━━━━━━
🎯 <b>Trade Setup:</b>
🎯 Best Entry: ${data['entry']} | ⏳ Hold Duration: {data['hold_time']}
🛑 SL: ${data['sl']} (+{data['sl_pct']}%) | ✅ TP1: ${data['tp1']} | ✅ TP2: ${data['tp2']} | ✅ TP3: ${data['tp3']}
📊 Leverage: {data['leverage']} | 🛡️ Risk: {data['risk']}
🧠 <i>{data['alpha']}</i>
🕒 <i>{self.get_timestamp()}</i>"""

    def funding_arbitrage(self, data):
        """Section 13: Funding Arbitrage Opportunity"""
        return f"""👑 <b>King Samrat Singh</b>
━━━━━━━━━━━━━━━━━━━━━━
💎 <b>FUNDING ARBITRAGE: RISK-FREE YIELD</b>
━━━━━━━━━━━━━━━━━━━━━━
🪙 <b>{data['symbol']}</b> {data['stars']} | 💰 <code>${data['price']}</code>
💼 Portfolio: ${data.get('portfolio', 10000):,} | Size: {data.get('size', 20)}%
🏦 {data['exchanges']}
📈 Direction: 🟡 NEUTRAL (Delta-Neutral) | 📊 Prob:  {data['prob_up']}%
━━━━━━━━━━━━━━━━━━━━━━
📊 <b>Funding:</b> Prev: {data['f_prev']} | Curr: {data['f_curr']} | Next: {data['f_next']}
💰 APR: {data['apr']} | 📊 Duration: {data['duration']} | 📈 Success Rate: {data['success_rate']}
💵 Cumulative Paid: {data['cumulative']} | ⏰ Next Funding: {data['next_fund_time']}
🌡️ Vol: {data['vol_level']} | 📊 Vol$: {data['vol_mult']} | 📈 Trend: {data['trend']}
💰 OI: {data['oi']} | 📐 RSI: {data['rsi']} | 🧠 Sent: {data['sentiment']}
━━━━━━━━━━━━━━━━━━━━━━
🎯 <b>Trade Setup:</b>
🎯 Best Entry: {data['entry']} | ⏳ Hold Duration: {data['hold_time']}
🛑 SL: {data['sl']} | TP: {data['tp']}
💰 Expected Profit: {data['expected_profit']} | 📊 7-Day: ~{data['profit_7d']}
🛡️ Risk: {data['risk']}
🧠 <i>{data['alpha']}</i>
🕒 <i>{self.get_timestamp()}</i>"""

    def funding_long_signal(self, data):
        """Section 14: Funding Rate Long Signal"""
        return f"""👑 <b>King Samrat Singh</b>
━━━━━━━━━━━━━━━━━━━━━━
🟢📈 <b>FUNDING RATE LONG SIGNAL</b>
━━━━━━━━━━━━━━━━━━━━━━
🪙 <b>{data['symbol']}</b> {data['stars']} | 💰 <code>${data['price']}</code>
💼 Portfolio: ${data.get('portfolio', 10000):,} | Size: {data.get('size', 6)}%
🏦 {data['exchanges']}
📈 Direction: 🟢 LONG | 📊 Prob:  {data['prob_up']}% | 📉 {data['prob_down']}%
━━━━━━━━━━━━━━━━━━━━━━
📊 <b>Funding:</b> Prev: {data['f_prev']} | Curr: {data['f_curr']} | Next: {data['f_next']}
📊 Signal Strength: {data['signal_strength']} | 🎯 R:R: {data['rr']} | 📈 Win Rate: {data['win_rate']}
📊 Momentum: {data['momentum']} | 📈 Percentile: {data['percentile']}
💵 Cumulative: {data['cumulative']} | ⏰ Next Funding: {data['next_fund_time']}
📊 Price-Funding Divergence: {data['divergence']}
🌡️ Vol: {data['vol_level']} | 📊 Vol$: {data['vol_mult']} | 📈 Trend: {data['trend']}
💰 OI: {data['oi']} | 📐 RSI: {data['rsi']} | 🧠 Sent: {data['sentiment']}
🐋 Whale: {data['whale']} | 💎 Smart: {data['smart']}
━━━━━━━━━━━━━━━━━━━━━━
🎯 <b>Trade Setup:</b>
🎯 Best Entry: ${data['entry']} | ⏳ Hold Duration: {data['hold_time']}
🛑 SL: ${data['sl']} (-{data['sl_pct']}%) | ✅ TP1: ${data['tp1']} | ✅ TP2: ${data['tp2']} | ✅ TP3: ${data['tp3']}
📊 Leverage: {data['leverage']} | 🛡️ Risk: {data['risk']}
💰 Funding Earned: ~{data['funding_earned']} per $10k (8h)
🧠 <i>{data['alpha']}</i>
🕒 <i>{self.get_timestamp()}</i>"""

    def funding_short_signal(self, data):
        """Section 15: Funding Rate Short Signal"""
        return f"""👑 <b>King Samrat Singh</b>
━━━━━━━━━━━━━━━━━━━━━━
🔴📉 <b>FUNDING RATE SHORT SIGNAL</b>
━━━━━━━━━━━━━━━━━━━━━━
🪙 <b>{data['symbol']}</b> {data['stars']} | 💰 <code>${data['price']}</code>
💼 Portfolio: ${data.get('portfolio', 10000):,} | Size: {data.get('size', 4)}%
🏦 {data['exchanges']}
📈 Direction: 🔴 SHORT | 📊 Prob:  {data['prob_up']}% | 📉 {data['prob_down']}%
━━━━━━━━━━━━━━━━━━━━━━
📊 <b>Funding:</b> Prev: {data['f_prev']} | Curr: {data['f_curr']} | Next: {data['f_next']}
📊 Signal Strength: {data['signal_strength']} | 🎯 R:R: {data['rr']} | 📈 Win Rate: {data['win_rate']}
📊 Momentum: {data['momentum']} | 📈 Percentile: {data['percentile']}
💵 Cumulative: {data['cumulative']} | ⏰ Next Funding: {data['next_fund_time']}
📊 Price-Funding Divergence: {data['divergence']}
🌡️ Vol: {data['vol_level']} | 📊 Vol$: {data['vol_mult']} | 📈 Trend: {data['trend']}
💰 OI: {data['oi']} | 📐 RSI: {data['rsi']} | 🧠 Sent: {data['sentiment']}
🐋 Whale: {data['whale']} | 💎 Smart: {data['smart']}
━━━━━━━━━━━━━━━━━━━━━━
🎯 <b>Trade Setup:</b>
🎯 Best Entry: ${data['entry']} | ⏳ Hold Duration: {data['hold_time']}
🛑 SL: ${data['sl']} (+{data['sl_pct']}%) | ✅ TP1: ${data['tp1']} | ✅ TP2: ${data['tp2']} | ✅ TP3: ${data['tp3']}
📊 Leverage: {data['leverage']} | 🛡️ Risk: {data['risk']}
💰 Funding Earned: ~{data['funding_earned']} per $10k (8h)
🧠 <i>{data['alpha']}</i>
🕒 <i>{self.get_timestamp()}</i>"""
