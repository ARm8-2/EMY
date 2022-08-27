
import discord
from utils.settings import color
from utils.resources import _getdescriptions


async def _help(self, ctx):
    embed = discord.Embed(title="**EMY** help", description=_getdescriptions("help"), color=color)
    await ctx.message.add_reaction('✅')
    await ctx.message.author.send(embed=embed)
