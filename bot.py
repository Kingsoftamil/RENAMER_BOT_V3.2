import asyncio
from pyrogram import Client, compose,idle
import os

from plugins.cb_data import app as Client2

TOKEN = os.environ.get("TOKEN", "6319901245:AAGYIqqehBexB3bGwXImxzmnYN-jinfZfGQ")

API_ID = int(os.environ.get("API_ID", "24665754"))

API_HASH = os.environ.get("API_HASH", "a0b67179736c205af31a20fc045670ce")

STRING = os.environ.get("STRING", "BQCpM4x0hBDkVXPMZesGGC2naIhz4QHS-0E5dWEElmCI6TQsVBm25KFG-ROHVQn1Hijd7bj4krNx9GN9mCCvEzmdYfLEry1rIXxzNFeH71PVsnGgb35hswc6mMsFXVVjWDODdl17KGNngVxnqEU5TB3RNUJCzDZK0joBmAef6yOnpEHa7Z5x-9MnP8IlDLWrX1znFMCWztlO-Y5d2ciXZkd8rCvwfJldr64UNZIRSZEwsi5PqpDd6hDelqWe4_YkhvS4v_A3h3lpY8tDyRg5bBlkHBEGuEKwEkC4yEL7s79bcTRwAApfdNO1fTd-vLYQ5YiyQKDN4ItatKiECez4HLHKAAAAATALTaMA")


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
