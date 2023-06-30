import os
import aiohttp
from os import getenv
from dotenv import load_dotenv
    
load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID", "1701859"))
API_HASH = getenv("API_HASH", "ebd582392a6d32290c7155925bee6d32")
BOT_TOKEN = getenv("BOT_TOKEN", "6096333459:AAHqBLMM0GVKhcJ5WA6BAywL8ILvYcwy_PY")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "1200"))
STRING_SESSION = getenv("STRING_SESSION", "BQC3EeilsfEVo_WvO7XPwGeEZ0EZXk602f7XgKAnOUxqwEx-NASLkot__UPt48xXf0x12Fs9F1RvNGe3PfL7xcGzl3rjasfcyuLjaZlIkf2rURvY3QKrlNOaC5msYkw3sYLrG60HaPdZRu61XAzBR1K0WPxnAHt0fPjibPG071Wv_WuU0fq3g2v7cxY57aDUNXnZ_KyLSr3ZTpZg4mcSmOQKyE2W7LyYxTRnqr8n7CB62fMLp4cZublwLA5peazu_kWkxjECz63UdBOrKxATV3T9A7cKd-w135k_G5-zQX0DYtohreeFrt68_PsMl2Syi-VZIxe3sPx4VLV2t2waMSNkAAAAAW4qInAA")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6096333459").split()))
aiohttpsession = aiohttp.ClientSession()
