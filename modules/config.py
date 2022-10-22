import os
import aiohttp
from os import getenv
from dotenv import load_dotenv
    
load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID", "27103643"))
API_HASH = getenv("API_HASH", "f0228dc23546b35de94efa2b47661949")
BOT_TOKEN = getenv("BOT_TOKEN", "5624486945:AAEESQnyMOn6xMeJ5zeslklhB74vAlBEpi4")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "900"))
STRING_SESSION = getenv("STRING_SESSION", "AQCTJOqtbSSsURI6edACxqShAMHPAoweYrPw2_bVX7__EI3vhKLO7QuDpgljmVXd7DMXkHUb_hecPtwbs6dTa-Y-c5yxwJywHJILyQiFHDb9SgpjplZ5ZCkU0cBYrUlX7BWm25RleziQ_G7NPUXbfa7Gb2x97Nq_JrVnh4yXfTf4nrXg5dE4uvQblYmEVZrscMU1RFVyr9__GYrVOyIh9NVkJGomzKBkhJJU8O_AL6B2Wti6C4JskzIw_c4gZ3fytugUr94NSPIKIp6tzpP4HLiZuRmPtM9aG_A9piDJCDPQ0wnwVezisqIbuT6tD1C_3usQh9woX5oPHG8q3BaG3ICNAAAAAVIVbuoA")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5683104617").split()))
aiohttpsession = aiohttp.ClientSession()
