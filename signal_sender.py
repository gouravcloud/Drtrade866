# signal_sender.py
import requests
import config

def send_signal(pair, direction, entry, sl, tp, rr, confidence):
    message = f"📢 *{pair} Signal Alert*\n\n" \
              f"📈 Direction: *{direction.upper()}*\n" \
              f"🎯 Entry: `{entry}`\n" \
              f"🛑 SL: `{sl}`\n" \
              f"🏁 TP: `{tp}`\n" \
              f"📊 RR: `{rr}`\n" \
              f"🔒 Confidence: {confidence}\n\n" \
              f"#DrTrade #Signals"

    payload = {
        "chat_id": config.CHAT_ID,
        "text": message,
        "parse_mode": "Markdown"
    }

    response = requests.post(
        f"https://api.telegram.org/bot{config.BOT_TOKEN}/sendMessage",
        json=payload
    )

    if not response.ok:
        raise Exception(f"Telegram Error: {response.text}")
