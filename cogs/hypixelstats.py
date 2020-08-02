import discord
from discord.ext import commands
from discord.ext import errors

class Hypixelstats(commands.Cog):
    def __init__(self, bot):
        self.bot = bot