import discord
from discord.ext import commands
from discord.ext.commands import errors

import aiohttp
from aiohttp import ClientSession


class Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot



def setup(bot):
    bot.add_cog(Commands(bot))