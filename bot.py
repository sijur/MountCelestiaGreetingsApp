import os

import discord
from dotenv import load_dotenv

from scripts.debug import botDebug

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

class GreetingsClient(discord.Client):
    async def on_message(self, message):
        if message.author == client.user:
            return


        if message.content.lower() == 'hello':
            await message.channel.send("Hello there {0}!".format(message.author.name))

client = GreetingsClient()
client.run(TOKEN)