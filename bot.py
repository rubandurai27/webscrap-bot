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
    
    
@app.on_message(filters.command(['start']))
def start(client, message):
            message.reply_text(text =f"Hello **{message.from_user.first_name }** \n\n **Iam Simple web scraper** 🕸 \n __SEND ME WEBSITE LINK AND GET THAT WEB SOURCE__",reply_to_message_id = message.message_id , parse_mode="markdown", reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Support 🇮🇳" ,url="https://t.me/lntechnical") ],
                 [InlineKeyboardButton("Subscribe 🧐", url="https://youtube.com/c/LNtechnical") ]          ]        ) )


@app.on_message(filters.regex("^(http|https|www\.)"))
def start(client, message):
    ms = message.reply_text("```Trying to web scrap .........```", reply_to_message_id = message.message_id)
    msg_id = message.chat.id
    html_url = message.text
    try:
    	page = re.get(html_url)
    	soup = BeautifulSoup(page,'html.parser')
    except Exception as e:
    	ms.edit(f"```Error : {e}```")
    	return
    f = open(f"{msg_id}.txt" , "w")
    f.write(str(soup.prettify()))
    f.close()

    caption = "Here Your Web Source"
    try:
    	app.send_document(message.chat.id ,document = f"{msg_id}.txt",caption = caption)
    except ValueError as ve:
    	ms.edit("```file Size value error")
    	os.remove(f"{msg_id}.txt")
    	return
    ms.delete()
    os.remove(f"{msg_id}.txt")
	
app.run()
