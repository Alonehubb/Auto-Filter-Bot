import re
import os
from os import environ
from pyrogram import enums
from Script import script
import asyncio
import json
from collections import defaultdict
from pyrogram import Client

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

#main variables
API_ID = int(environ.get('API_ID', '27662412'))
API_HASH = environ.get('API_HASH', '4a695060ecd737dffa9e92c540b46ed2')
BOT_TOKEN = environ.get('BOT_TOKEN', '7613189441:AAEjn2_OWE0hqIDvKpIChgKSVT2LS0KNeow')
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '6847319298').split()]
USERNAME = environ.get('USERNAME', 'https://telegram.me/mrboy638')
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1002170835362'))
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-1002370744720').split()]
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://vzdkz:cmo941iJf72S3MUP@cluster0.2vib8.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DATABASE_URI2 = environ.get('DATABASE_URI2', "mongodb+srv://vzdkz:cmo941iJf72S3MUP@cluster0.2vib8.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DATABASE_NAME = environ.get('DATABASE_NAME', "TELEGRAM_BOT_INFO")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')
LOG_API_CHANNEL = int(environ.get('LOG_API_CHANNEL', '-1002410598235'))
QR_CODE = environ.get('QR_CODE', 'https://graph.org/file/cf0815db33c71115b208a.jpg')

#this vars is for when heroku or koyeb acc get banned, then change this vars as your file to link bot name
BIN_CHANNEL = int(environ.get('BIN_CHANNEL', '-1002308573369'))
URL = environ.get('URL', '')

# verify system vars
IS_VERIFY = is_enabled('IS_VERIFY', True)
LOG_VR_CHANNEL = int(environ.get('LOG_VR_CHANNEL', '-1002349501310'))
TUTORIAL = environ.get("TUTORIAL", "https://t.me/xmovieshub56")
TUTORIAL2 = environ.get("TUTORIAL2", "https://t.me/xmovieshub56")
TUTORIAL3 = environ.get("TUTORIAL3", "https://t.me/xmovieshub56")
VERIFY_IMG = environ.get("VERIFY_IMG", "https://graph.org/file/45a270fc6a0a1c183c614.jpg")
SHORTENER_API = environ.get("SHORTENER_API", "e27949c396504dca50e6caed52b70917f00593c9")
SHORTENER_WEBSITE = environ.get("SHORTENER_WEBSITE", "linkpays.in")
SHORTENER_API2 = environ.get("SHORTENER_API2", "3f59866fff2e9dda7fe21ad1439705357cd13030")
SHORTENER_WEBSITE2 = environ.get("SHORTENER_WEBSITE2", "gplinks.com")
SHORTENER_API3 = environ.get("SHORTENER_API3", "beede0b297fcecb40ca4b963c37e599140ce8923")
SHORTENER_WEBSITE3 = environ.get("SHORTENER_WEBSITE3", "atglinks.com")
TWO_VERIFY_GAP = int(environ.get('TWO_VERIFY_GAP', "3600"))
THREE_VERIFY_GAP = int(environ.get('THREE_VERIFY_GAP', "21600"))

# languages search
LANGUAGES = ["hindi", "english", "telugu", "tamil", "kannada", "malayalam"]

auth_channel = environ.get('AUTH_CHANNEL', '-1002452396602')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
SUPPORT_GROUP = int(environ.get('SUPPORT_GROUP', '-1002220096661'))

# bot settings
AUTO_FILTER = is_enabled('AUTO_FILTER', True)
PORT = os.environ.get('PORT', '8080')
MAX_BTN = int(environ.get('MAX_BTN', '8'))
AUTO_DELETE = is_enabled('AUTO_DELETE', True)
DELETE_TIME = int(environ.get('DELETE_TIME', 600))
IMDB = is_enabled('IMDB', False)
FILE_CAPTION = environ.get('FILE_CAPTION', f'{script.FILE_CAPTION}')
IMDB_TEMPLATE = environ.get('IMDB_TEMPLATE', f'{script.IMDB_TEMPLATE_TXT}')
LONG_IMDB_DESCRIPTION = is_enabled('LONG_IMDB_DESCRIPTION', False)
PROTECT_CONTENT = is_enabled('PROTECT_CONTENT', False)
SPELL_CHECK = is_enabled('SPELL_CHECK', True)
LINK_MODE = is_enabled('LINK_MODE', True)
PM_SEARCH = is_enabled('PM_SEARCH', False)
