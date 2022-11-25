import os
import aiohttp
from os import getenv
from dotenv import load_dotenv
    
load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID", "24547069"))
API_HASH = getenv("API_HASH", "35b8c016ea0cb8b7f88cdd1626e30123")
BOT_TOKEN = getenv("BOT_TOKEN", "5624694570:AAGIoOZZox5gAqyXroQ_84GfJMsMOlIxgiE")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "1200"))
STRING_SESSION = getenv("STRING_SESSION", "AQCZrdUms7FqhCDHBYwUOzhENK1zF5vDFWisiu7PGpH05QnU8U0wKhLMFhE5hM5Sane4Y0e3fxtS2UzwOz8zh5n9EoLZFWzU-iZnR3ln9ESUUFLM93aSpzUeiBXd5QDZC6m8LdCKYu_8yLkPkVBrH9jDL7jEj6qF0O_qM3p3ZitCp2KZKW1b5JoPjoKLdevHEFgQfhUNmqtJNqmR7pY-zF66yKcFaQFz5bhOOXYogpOzsNT0_DBNQw5DrAbwJquxyvK9ofkzYlw-xBdPi-0JRa1XxDxJM8LUdYqcL2zvQ3SUfo9SdFRQmcNBMlYE6oW78vSjtIcjdd2_Km-hiI6iXVgrAAAAAU0WLlEA")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5768114635 5737833424").split()))
aiohttpsession = aiohttp.ClientSession()
