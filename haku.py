from pyrogram import Client
import time

api_id = '1634450'
api_hash = '1a42e816cae8d86e71a4c466bba19b8c'
sstring = 'BQAY8JIAPR9nfALn38XmPS5HaHTGJpauFcu8Em78JchW5WGr1STQSy3mCFqablSbHSZM9z2W2IK4Jn1k_iS4CDrX7ggLo7sSH6_XqfMhIp3GGAuy9QLiCfkM2DyVoh9vuZn5GLOcPK9SklT0yN6K4Ubf8xNDPaIcnvWnIBn2ZYw8jVJjEeWapAx59QCBDrNP9kxylrstQDC7LSTjK0vaiMMPalA2CvP8ndhSqYyanxpDqLMtMhOKn9U0hXzigv2elueku3SSCaRaYGmJMatWU9C5SrkHvnGHD35w7BMu9zm4tHc1PGW54u3MeZANKG5vSa8NEJjcEemB_je2pr8BcsfLxDaPvAAAAAF7EvbWAA'

app = Client(name="haku", session_string=sstring, api_id=api_id, api_hash=api_hash)

def send_message():
    chat_id = int(1207941747)
    message = 'cgcast ᴀsʜʜᴜᴘᴘᴀɴɴ ᴏᴍᴍ33ᴄᴋᴋᴋᴋᴋ ᴅɪ ʙᴇʏᴏʜʜʜʜ'
    app.send_message(chat_id=chat_id, text=message)

with app:
    while True:
        send_message()
        time.sleep(10800)