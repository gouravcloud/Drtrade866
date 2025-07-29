# webhook.py
from flask import Flask, request, jsonify
import config
from signal_sender import send_signal

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json

    if not data or data.get("token") != config.WEBHOOK_TOKEN:
        return jsonify({"error": "Unauthorized"}), 403

    try:
        pair = data.get("pair")
        direction = data.get("direction")
        entry = float(data.get("entry"))
        sl = float(data.get("sl"))
        tp = float(data.get("tp"))
        rr = round(abs(tp - entry) / abs(entry - sl), 2)
        confidence = data.get("confidence", "⭐⭐⭐")

        send_signal(pair, direction, entry, sl, tp, rr, confidence)
        return jsonify({"status": "Signal sent"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7860)
