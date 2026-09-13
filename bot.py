import os
import requests
from dotenv import load_dotenv
from crewai.tools import tool

load_dotenv()

bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
chat_id = os.getenv("TELEGRAM_CHAT_ID")

@tool("Telegram Tool")
def send_message(text: str) -> str:
    """Use this tool to send finalized text messages to a Telegram channel. #message for the agent on how to use this tool.
    The input should be the exact text you want to send."""

    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {"chat_id":chat_id,
                "text":text
               }
    results = requests.post(url, json=payload)
    if results.status_code == 200:
        return "Message sent successfully."
    else:
        return f"Message sent failed!!! reason {results.text}"



