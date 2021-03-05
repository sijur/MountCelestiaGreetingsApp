import os

import discord
from dotenv import load_dotenv

from scripts.debug import botDebug

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

class GreetingsClient(discord.Client):
    pass

client = GreetingsClient()
client.run(TOKEN)