import streamlit as st
import requests

BOT_TOKEN = "8323795138:AAEv6jwYH-nn8rhp4bp4ZETudDwg14SKSRM"
CHAT_ID = "-1002736241048"

st.set_page_config(page_title="DrTrade Signal Sender", layout="centered")
st.title("📡 DrTrade Signal Sender")
st.markdown("Send high‑probability manual signals to your Telegram channel (M15)")

pair = st.selectbox("Select Pair", ["XAU/USD", "EUR/USD", "BTC/USD"])
direction = st.radio("Trade Direction", ["BUY", "SELL"], horizontal=True)
entry = st.text_input("Entry Price")
sl = st.text_input("Stop Loss")
tp = st.text_input("Take Profit")
risk = st.slider("Risk %", 0.5, 5.0, 1.0, 0.5)
confidence = st.slider("Confidence (⭐)", 1, 5, 4)

if st.button("🚀 Send Signal"):
    if not (entry and sl and tp):
        st.warning("Please fill Entry, SL and TP.")
    else:
        message = f"""
🔥 15M Trade Signal

{'📈' if direction == 'BUY' else '📉'} Pair: {pair}
🕐 Timeframe: 15 Min
📍 Type: {direction}
🎯 Entry: {entry}
🛑 SL: {sl}
✅ TP: {tp}
📊 Risk: {risk:.1f}% | RR: Custom
💡 Confidence: {'⭐' * confidence}

#DrTrade #ManualSignal
        """
        resp = requests.post(
            f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
            data={"chat_id": CHAT_ID, "text": message}
        )
        if resp.status_code == 200:
            st.success("Signal sent successfully ✅")
        else:
            st.error(f"Failed to send: {resp.json()}")
