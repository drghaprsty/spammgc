import random
import time
import os
from pyrogram import Client
from dotenv import load_dotenv
import logging

load_dotenv(".env")

api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")
sstring = os.getenv("SESSION")

app = Client(name="haku", session_string=sstring, api_id=api_id, api_hash=api_hash)

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

messages = [
    ".gcast ᴀsᴜᴘᴀɴ ᴠɪʀᴀʟ ᴅɪᴘʀᴏꜰɪʟᴋᴜ",
    ".gcast ᴀᴅᴀ ʏɢ ᴍᴀɴᴛᴀᴘ ᴅɪʙɪᴇᴏᴋᴜ",
    ".gcast ᴘᴇᴍᴇʀsᴀᴛᴜ ʙᴀɴɢsᴀ ʙɢᴛ ᴅɪᴘʀᴏꜰɪʟᴋᴜʜ",
    ".gcast ʏɢ ʙɪᴋɪɴ ᴇɴᴀᴋ ᴀᴅᴀ ᴅɪʙɪᴏᴇᴋᴜ",
    ".gcast sᴋᴀɴᴅʜᴀʟ ᴠɪʀᴀʟᴇ ᴅɪʙɪᴇᴜᴏᴋᴜ",
    ".gcast ᴀᴅᴀ ʏᴀɴɢ ʟᴀɢɪ ʀᴀᴍᴇ ᴅɪᴛɪᴋᴛᴏᴋ ᴅɪʙɪʏᴏᴋᴜʜ",
]

def send_message():
    x = app.get_me()
    chat_id = x.id
    message = random.choice(messages)
    app.send_message(chat_id=chat_id, text=message)
    logger.info(f"Message sent to chat {chat_id}: {message}")

with app:
    while True:
        send_message()
        time.sleep(1200)
