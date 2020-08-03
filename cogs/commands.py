import discord
from discord.ext import commands
import aiohttp


class Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def hello(self, ctx):
        await ctx.send(f"Hello" {member.mention})


def setup(bot):
    bot.add_cog(Commands(bot))