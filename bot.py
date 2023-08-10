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
    ".gcast AAD4 Y4ANG LAG91 VIR4AL DIBI0OHKOUUU🥵",
    ".gcast 𝚅𝙸𝚁a𝙰𝙻 𝚃𝙸𝙺𝚃𝙾o𝙺 𝙳𝙸𝙿𝚁𝙾𝙵𝙸𝙻𝙺i𝚄𝙷🥵",
    ".gcast ASUEP4AN MANJAAHHH DIBIEO0HHKUH🥵",
    ".gcast BANYAK KONTHEN HIJ4B DIBIE0H🥵",
    ".gcast SK4NDAL VID3O V1R4LS DIPROF1LKUH🥵",
    ".gcast AD4H Y4N9 LAG1 V1RAL BANG3T DIB1OHKUUU",
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
