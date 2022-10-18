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
        photo=f"https://te.legra.ph/file/ce63cc853dc7f605d2f36.jpg",
        caption=f"""**
『It's a Music bot without lag and struck .
  It's a official Music bot of Team DC 
Nb : Bot and Userbot are locked by owner ,
     who wish to add this bot to your group,
     then , contact @KRISHNA_THULSI』
**""",
reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "『Stenzle』", url=f"https://t.me/Stenzle_MariaGbot?startgroup=true"),
                    InlineKeyboardButton(
                        "『RUDRA_BHADRA』", url=f"https://t.me/Rudra_BhadraGbot?startgroup=true"),
                    InlineKeyboardButton(
                        "『TEAM DC』", url=f"https://t.me/KRISHNA_THULSI") 
                ]
            ]
        ),
     )
    
    
@Client.on_message(commandpro(["/start", "/alive", "blackcat"]) & filters.group & ~filters.edited)
async def start(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/0a553449a9518e8adfa70.jpg",
        caption=f"""**𝙾𝙵𝙵𝙸𝙲𝙸𝙰𝙻 𝐌𝐔𝐒𝐈𝐂 Bot of TEAM DC**,
        it's A 💯% LAG AND STRUCK FREE MUSIC BOT , 
        IT KEEP CLEAN YOUR CHAT WHEN IT WORK ON YOUR CHAT,
        3hrs Unlimited Playing without Lag       
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "『Stenzle』", url=f"https://t.me/Stenzle_MariaGbot?startgroup=true"),
                    InlineKeyboardButton(
                        "『RUDRA_BHADRA』", url=f"https://t.me/Rudra_BhadraGbot?startgroup=true"),
                    InlineKeyboardButton(
                        "『TEAM DC』", url=f"https://t.me/KRISHNA_THULSI")
                ]
            ]
        ),
    )

