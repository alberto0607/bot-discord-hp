import os
import asyncio
import discord
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = str(os.getenv('DISCORD_TOKEN'))

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='$', intents=intents)


def load():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            bot.load_extension(f'cogs.{filename[:-3]}')

load()

bot.run(TOKEN)
