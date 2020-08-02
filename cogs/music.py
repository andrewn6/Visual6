import discord
from discord.ext import commands
from discord.ext import errors
import youtube_dl

class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot