import asyncio
from time import time
from datetime import datetime
from modules.helpers.filters import command
from modules.helpers.command import commandpro
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)
    
   

@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/82cea8cd9e2cfa08b8f3e.jpg",
        caption=f"""**
『It's a Music bot without lag and struck .
  It's a official Music bot of @kk_kovilakam 
Nb : Bot and Userbot are locked by owner ,
     who wish to add this bot to your group,
     then , contact @CRUAL_MIND』
**""",
reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "『🅖🅡🅞🅤🅟』", url=f"https://t.me/Kerala_Cousinsofficial")
                ]
            ]
        ),
     )
    
    
@Client.on_message(commandpro(["/start", "/alive", "blackcat"]) & filters.group & ~filters.edited)
async def start(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/82cea8cd9e2cfa08b8f3e.jpg",
        caption=f"""**ഇപ്പോഴും ജീവനോടെ ഉണ്ട് . ചത്തിട്ടില്ല**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "GrouP", url=f"https://t.me/Kerala_Cousinsofficial")
                ]
            ]
        ),
    )

