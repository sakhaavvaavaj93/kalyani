import os
import aiohttp
from os import getenv
from dotenv import load_dotenv
    
load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID", "27103643"))
API_HASH = getenv("API_HASH", "f0228dc23546b35de94efa2b47661949")
BOT_TOKEN = getenv("BOT_TOKEN", "5749790297:AAHlz7W8-3dA-zDf81KXQGeaokGpu9OWPag")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "900"))
STRING_SESSION = getenv("STRING_SESSION", "AQBtPhRJU9d--DtGo14-q8YjNY1sAAKK0tT2lLBvxf0KxTdKFM_xrFGBxGZVpFQ4RI3Qg576yAdqCbJwPyz4T4QIKVYJVHycDj_T9eWjT-0pdJn87uM5G_xCkKWdirhHpmDuqyn8fQ2zD4Mgwwx04qR0wqfMk51P9s7FqrWOqyJMhTj0pnhSCEnC_F4hkVY3MNtzES5jRxQQvZWyLkwlD9C4n7cXqSa8R23xrkawQ64sLLw5d7gxhrkWkUSfj71PmcyCvnpR8ryxzLe6D2Z9SPHjYbDTPGYPXM-hrqUdt20g1C-mCv5mqee_fRZ6ZxLAFuGmkgqP9gduhQiWdPaNf_beAAAAAVIVbuoA")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5683104617").split()))
aiohttpsession = aiohttp.ClientSession()
