import random
from pyrogram import Client
import time

api_id = '1634450'
api_hash = '1a42e816cae8d86e71a4c466bba19b8c'
sstring = 'BQAY8JIAL5G47q8ilduioehpYyKc7lSF-qqh3PX_Zfjs0S2I_F567ePC-HqsDzARZwLbYsoNKdt4NunkDfbiEkAFnCWFQmLaXu6c94-NE4Rggiw-eQvRhtpeNIciGKbGfAp7xgovZh7kt8cJMGF1pr1jeRqAyMxz3Kymvs-_VvTEf4eEjI8ly7CBfd3kOyzGqZZTteCm9xXoQi4DmCZ57OZx3JU_DkSObNvz3xloGPACWUO89xyvS-Juw3mMKoU-ilgtgpuKzQ78MP1-5xgG3W51K77ksX1tWnGwHV6E1UGK9NaRWF1WF13LmnDn4LS6SsATyF9kiebZtNXourHacJpt6XKxuQAAAAA4nAPUAA'

app = Client(name="haku", session_string=sstring, api_id=api_id, api_hash=api_hash)

messages = [
    ".gcast AAD4 Y4ANG LAG91 VIR4AL DIBI0OHKOUUU🥵",
    ".gcast 𝚅𝙸𝚁a𝙰𝙻 𝚃𝙸𝙺𝚃𝙾o𝙺 𝙳𝙸𝙿𝚁𝙾𝙵𝙸𝙻𝙺i𝚄𝙷🥵",
    ".gcast ASUEP4AN MANJAAHHH DIBIEO0HHKUH🥵",
    ".gcast BANYAK KONTHEN HIJ4B DIBIE0H🥵",
    ".gcast SK4NDAL VID3O V1R4LS DIPROF1LKUH🥵",
    ".gcast AD4H Y4N9 LAG1 V1RAL BANG3T DIB1OHKUUU",
]

def send_message():
    chat_id = int(949748692)
    message = random.choice(messages)
    app.send_message(chat_id=chat_id, text=message)

with app:
    while True:
        send_message()
        time.sleep(1200)
