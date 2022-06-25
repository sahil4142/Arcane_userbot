import os
from os import getenv

from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")
que = {}
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "555534224").split()))
API_ID = int(getenv("API_ID", "11508502"))
API_HASH = getenv("API_HASH", "3e6e5be80d5c89ff19b5e5fb7bfaa0f4")
LOG_GROUP = getenv("LOG_GROUP", "")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "")
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "")
SPOTIFY_USERNAME = getenv("SPOTIFY_USERNAME", "")
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://XdUserbot:XdUserbot@cluster0.n9nep.mongodb.net/?retryWrites=true&w=majority")
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/73ec771be88de09d0392a.jpg")
DB_URL = getenv("DATABASE_URL", "")
STRING_SESSION1 = getenv("STRING_SESSION1", "")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")


