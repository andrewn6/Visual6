# Error handling for the commands and bot permmisions
import discord
from discord.ext import commands
from discord.ext.commands.errors import *


class Errors(commands.Cog):
    def __init__(self, bot):
        self.bot



def setup(bot):
    bot.add_cog(Errors(bot))