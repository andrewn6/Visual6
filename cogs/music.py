import discord
from discord.ext import commands
from discord.ext.commands import errors
import youtube_dl

class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot




def setup(bot):
    bot.add_cog(Music(bot))