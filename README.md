# Algorithmic Momentum Trading Bot

An automated 15-minute momentum breakout trading bot utilizing multi-timeframe 1H trend alignment and strict risk-management rules.

## Strategy Overview
* **Macro Filter:** 1H EMA 200 trend alignment.
* **Momentum & Trigger:** 15m candle close beyond the previous 20 bars with volume confirmation.
* **Risk Management:** Dynamic stop-loss using swing structure and ATR, paired with structured take-profits.
* **Execution:** Designed with safety checks, optional demo bridge integration, and strict TTL order management.
