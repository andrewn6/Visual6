import discord
from discord.ext import commands


import json
import asyncio
import os


#def read(FileNameAndPath):
  #  with open(FileNameAndPath, "r") as f:
     #   return json.load(f)

#private = read("./private/tokens.json")
#data = read("./private/data.json")

#token = private.get("token")

#activity_1 = data.get("activity_1")

#activity_2 = data.get("activity_2")

bot =  commands.Bot(command_prefix="!v")
token = "NzAzMjgwMTg1NDY1NjM0ODU3.XqMStg.xhQANolDBuzYk7mO57noqLBGbXQ"
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

if __name__ == "__main__":
    bot.run(token)