import os
import aiohttp
from os import getenv
from dotenv import load_dotenv
    
load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID", "24547069"))
API_HASH = getenv("API_HASH", "35b8c016ea0cb8b7f88cdd1626e30123")
BOT_TOKEN = getenv("BOT_TOKEN", "5749790297:AAHlz7W8-3dA-zDf81KXQGeaokGpu9OWPag")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "900"))
STRING_SESSION = getenv("STRING_SESSION", "AQBs-ZZmR08sp4EGNt-l8oUDXy6871VxgxnadluYLt7sZLoJQR-gs2Trb5IxcZzeeexCE66hpmM6J0h3pznjzzhUp_As4ROgsy7lxQIhKzqcxHYZcoHbvfDqDnQBVtnYos-NMgELad1mfjkUaxpzaPsfEutMitDnscWMKQJ_snkpMfjxuwzoG9zT5PJAN5DYyjCibJ7woqYrX0z78flujvZcW4dZ6lPdm5o2OwvSuilyZ63usN2azEBjewg6GfcCWNYYyJNp2TW2WcB0Gg3prqpW5eDLR0oT8dWQSA-m_w48Y-d5Kto5hkVo8ImGOjH6G80jah_FnTCAxh3LmYO2GsW8AAAAAVb91TwA")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5683104617").split()))
aiohttpsession = aiohttp.ClientSession()
