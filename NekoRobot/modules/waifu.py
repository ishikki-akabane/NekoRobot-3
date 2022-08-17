#fixed swaifu module @ishikki_akabane
import requests
import nekos
import random
from telegram import ParseMode
from telegram.ext import CommandHandler, run_async

from NekoRobot import dispatcher
import NekoRobot.modules.waifu_string as waifu_string

url_sfw_1 = "https://api.waifu.pics/sfw/" 
url_sfw_2 = "https://nekos.best/"


def waifu(update, context):
    try:
        msg = update.effective_message
        # API (DON'T EDIT)
        url = f'https://api.animeepisode.org/waifu/'
        result = requests.get(url).json()
        img = result['Character_Image']
        # Message (EDIT THIS PART AS HTML *IF YOU WANT*)
        text = f'''
<b>Name :</b> <code>{result['Character_Name']}</code>
        
<b>Anime :</b> <code>{result['Anime_name']}</code>
'''
        msg.reply_photo(photo=img, caption=text, parse_mode=ParseMode.HTML)

    except Exception as e:
        text = f'<b>Error</b>: <code>' + e + '</code>'
        msg.reply_text(text, parse_mode=ParseMode.HTML)

        

def waifus(update, context):
    update.effective_message.reply_photo(random.choice(waifu_string.WAIFUS))

    

def swaifu(update, context):
    msg = update.effective_message
    url = f"{url_sfw_1}waifu" 
    result = requests.get(url).json()
    img = result['url']
    msg.reply_photo(photo=img)
    
    

WAIFU_HANDLER = CommandHandler('waifuinfo', waifu, run_async=True)
WAIFUS_HANDLER = CommandHandler("waifus", waifu, run_async=True)
SWAIFU_HANDLER = CommandHandler('swaifu', swaifu, run_async=True)

dispatcher.add_handler(WAIFU_HANDLER)
dispatcher.add_handler(SWAIFU_HANDLER)
dispatcher.add_handler(WAIFUS_HANDLER)

__mod_name__ = "Wᴀɪғᴜ"

__help__ = """
❍ `/swaifu` : Gives random image of best selected waifus.
❍ `/waifus` : Gives random image of waifu
❍ `/waifuinfo` : Gives random image of waifu with info.
"""

__handlers__ = [
  WAIFU_HANDLER,
  WAIFUS_HANDLER,
  SWAIFU_HANDLER
]
