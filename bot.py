import os

import discord
from dotenv import load_dotenv

from scripts.debug import botDebug

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

botDebug.logling()

class MyClient(discord.Client):
    pass

client = MyClient()
client.run(TOKEN)