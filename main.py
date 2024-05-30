import discord
import os
import pickle
from dotenv import load_dotenv
from samobot import SamoBot
import logging
from datetime import datetime
load_dotenv()

logger = logging.getLogger("discord")
logger.setLevel(logging.DEBUG)

fn = f'\\logs\\discord_{datetime.now().strftime("%y%m%d_%H%M%S")}.txt'
handler = logging.FileHandler(filename="discord.log", encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

f = open('banned_words.txt')


token = str(os.getenv("TOKEN"))

terms = f.read().splitlines()
f.close()

intents = discord.Intents.default()
intents.message_content = True

with open('saved_brainrot.pkl', 'rb') as f:
    brainrot_count = pickle.load(f)

with open('my_id', 'r') as f:
    my_id = f.read()

bot = SamoBot(terms, brainrot_count=brainrot_count, my_id=my_id, intents=intents)
bot.run(os.getenv("TOKEN"))

