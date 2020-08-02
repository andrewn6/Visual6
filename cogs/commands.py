import discord
from discord.ext import commands
import aiohttp


class Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        