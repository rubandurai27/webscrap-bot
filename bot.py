import os
import requests as re
from bs4 import BeautifulSoup
from pyrogram import Client, filters
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup
)

TOKEN = os.environ.get("TOKEN", "")

API_ID = int(os.environ.get("API_ID", 12345))

API_HASH = os.environ.get("API_HASH", "")

app = Client(
        "webscrap",
        bot_token=TOKEN,
        api_id=API_ID,
        api_hash=API_HASH,
    )

START_TEXT  = """Hello **{}** \n\n **Iam Simple web scraper** 🕸 \n __SEND ME WEBSITE LINK AND GET THAT WEB SOURCE__"""
START_BUTTONS = InlineKeyboardMarkup(
                      [[
                       InlineKeyboardButton("Support 🇮🇳" ,url="https://t.me/lntechnical")
                      ],[
                       InlineKeyboardButton("Subscribe 🧐", url="https://youtube.com/c/LNtechnical")]]
                       )

@app.on_message(filters.command(['start']))
def start(client, message):
    await update.reply_text(
        text=START_TEXT.format(update.from_user.mention),
        reply_markup=START_BUTTONS,
        disable_web_page_preview=True,
        quote=True
    )
	
app.run()
