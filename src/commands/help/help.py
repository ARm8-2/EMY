
import discord
from discord.ext import commands
from utils.resources import _getdescriptions
from utils.settings import color


async def _help(ctx: commands.Context):
    embed = discord.Embed(title="**EMY** help", description=_getdescriptions("help"), color=color)
    await ctx.message.add_reaction('✅')
    await ctx.message.author.send(embed=embed)
