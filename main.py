import discord
from discord.ext import commands
from discord.ext.commands.errors import *

import json
import asyncio
import os


def read(FileNameAndPath):
    with open(FileNameAndPath, "r") as f:
        return json.load(f)

private = read("./private/tokens.json")
data = read("./private/data.json")

token = private.get("token")

activity_1 = data.get("activity_1")

activity_2 = data.get("activity_2")

bot =  commands.Bot(command_prefix="!v")

extensions = [
    "cogs.modcommands"
    "cogs.commands"
    "cogs.hypixelstats"
    "cogs.music"
]

for ext in extensions:
    bot.load_extension(bot)
    
@bot.event
async def on_ready():
    print('Connected')
    print("bot.cogs")
    print(len(bot.guilds))
    print(len(bot.users))
    while True:
        asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(name=activity_2))
        asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(name=activity_1))
        asyncio.sleep(12)