import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

intents = discord.Intents.default()

"""INTENTS HERE"""

bot = commands.Bot(command_prefix="!", intents=intents)

"""COMMANDS HERE"""

if __name__ == "__main__":
    load_dotenv()
    bot.run(os.getenv('TOKEN'))
