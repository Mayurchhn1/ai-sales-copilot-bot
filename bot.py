from fastapi import FastAPI, Request
import requests

app = FastAPI()

BOT_TOKEN = "8671553804:AAGZlFDamXm4Kn1fw5s6MrjUVwwXGrkDUJE"
TELEGRAM_API = f"https://api.telegram.org/bot{BOT_TOKEN}"

def send_message(chat_id, text):
    requests.post(f"{TELEGRAM_API}/sendMessage", json={
        "chat_id": chat_id,
        "text": text
    })

@app.get("/")
def home():
    return {"status": "Bot is running 🚀"}

@app.post("/webhook")
async def webhook(req: Request):
    data = await req.json()

    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        text = data["message"].get("text", "")

        if text == "/start":
            send_message(chat_id, "Welcome to AI Sales Copilot 🚀")

        elif text == "/assist":
            send_message(chat_id, "Tell me your sales goal")

        else:
            send_message(chat_id, f"You said: {text}")

    return {"ok": True}