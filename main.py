from flask import Flask, request
import requests

app = Flask(__name__)

BOT_TOKEN = "8933983896:AAGlDPlT8R1RFpvcjH2DXFoYwcaYcew-omw"
CHAT_ID = "-1003948216649"

@app.route("/")
def home():
    return "Nexus Online"

@app.route("/webhook", methods=["POST"])
def webhook():

    data = request.json

    mensaje = data.get("message", "Sin señal")

    requests.post(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        json={
            "chat_id": CHAT_ID,
            "text": mensaje
        }
    )

@app.route("/test")
def test():
    requests.post(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        json={
            "chat_id": CHAT_ID,
            "text": "TEST DESDE RAILWAY"
        }
    )
    return "OK"
    return {"status": "ok"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
