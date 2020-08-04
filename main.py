import discord
from discord.ext import commands
import json

import asyncio
import os

import dotenv
from dotenv import load_dotenv

load_dotenv()

def read(FileNameAndPath):
    with open(FileNameAndPath, "r") as f:
        json.load(f)
        

bot =  commands.Bot(command_prefix="!v")

token = os.getenv('client_id')


for filename in os.listdir("/home/andrew/Documents/visualbot/bot/cogs"):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

@bot.event
async def on_ready():
    print('Connected')
    print("bot.cogs")
    print(len(bot.guilds))
    print(len(bot.users))

if __name__ == "__main__":
    bot.run(token)