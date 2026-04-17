from fastapi import FastAPI, Request
import requests

app = FastAPI()

BOT_TOKEN = "8671553804:AAEpdPaohxoSB3VZ2N0I7ngGTiwsAMaiQhQ"
TELEGRAM_API = f"https://api.telegram.org/bot{BOT_TOKEN}"

def generate_response(user_input):
    return f"🤖 AI Suggestion:\n\nBased on your input: '{user_input}', focus on value-driven messaging and clear CTA."

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
            response = generate_response(text)
            send_message(chat_id, response)

    return {"ok": True}