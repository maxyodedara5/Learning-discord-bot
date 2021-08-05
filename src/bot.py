import discord
from discord.ext import commands
from discord.flags import Intents
from dotenv import load_dotenv
from os import getenv

load_dotenv()

token = getenv("TOKEN")

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix = "!", intents=intents)


bot.load_extension("somecommands")



bot.run(token)
