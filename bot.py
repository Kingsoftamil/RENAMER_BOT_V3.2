import asyncio
from pyrogram import Client, compose,idle
import os

from plugins.cb_data import app as Client2

TOKEN = os.environ.get("TOKEN", "6319901245:AAGYIqqehBexB3bGwXImxzmnYN-jinfZfGQ")

API_ID = int(os.environ.get("API_ID", "24665754"))

API_HASH = os.environ.get("API_HASH", "a0b67179736c205af31a20fc045670ce")

STRING = os.environ.get("STRING", "")


bot = Client(

           "Renamer",

           bot_token=TOKEN,

           api_id=API_ID,

           api_hash=API_HASH,

           plugins=dict(root='plugins'))
           

if STRING:
    apps = [Client2,bot]
    for app in apps:
        app.start()
    idle()
    for app in apps:
        app.stop()
    
else:
    bot.run()
