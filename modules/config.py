import os
import aiohttp
from os import getenv
from dotenv import load_dotenv
    
load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID", "18976857"))
API_HASH = getenv("API_HASH", "c294098eb66ba527caf82c974d655a1e")
BOT_TOKEN = getenv("BOT_TOKEN", "5521157144:AAHlTJZYNjIl_chsEZSi2DmCNMwvjfIjQHM")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "900"))
STRING_SESSION = getenv("STRING_SESSION", "AQA4BdG2SwDz7ro5I_vQon4Jx34LPFGhnpl9pMUViULGa_jSTJQ1qkshhsQOLKozGJAf9nz0qmRZmfpC2HfGjCu6h0BO_YPWv3hKXUcdgiOWyBeJMx1YjTYwhwFcMLbG4XmJrcuXEZHU6eeAplD3EjeT3iJAk3BFB7FsokhBt-d16wqkuFogqN74QsoQKN8EMntNxq8NLvqkwicdUJ7JIN-6GjKg75i3Vg0OIm2OoIJlQu3VP8EXUkF_Px7xlBBc0W-W5KQOG-UcEdoYtyqIOpoTl5bv3wJhg9wq6JPNZSHwcYShIlkavU8n8QQVoNfT0lLnFjc_H6SdPDkd93ABl3QgAAAAATUFo1MA")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5616310867").split()))
aiohttpsession = aiohttp.ClientSession()
