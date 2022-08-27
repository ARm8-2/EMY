
from utils.settings import color
from utils.resources import _changeprefix

import discord
from discord.ext import commands


class Utility(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(name='ping')
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def _ping(self, ctx):
        embed = discord.Embed(title="", description=f"Latency: {round(self.client.latency * 1000)}ms", color=color)
        await ctx.send(embed=embed)

    @commands.command(name='changeprefix', aliases=['prefix'])
    @commands.has_permissions(administrator=True)
    async def _changeprefix(self, ctx, prefix):
        await _changeprefix(ctx, prefix)

    @commands.command(name='bot')
    async def _bot(self, ctx):
        embed = discord.Embed(title='', description='', color=color)
        embed.set_author(name=self.client.user.name, icon_url=self.client.user.avatar_url)
        embed.add_field(name=f"```Latency:```", value=f"{round(self.client.latency * 1000)}ms", inline=False)
        embed.add_field(name=f"```id:```", value=f"{self.client.user.id}", inline=False)
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Utility(client))
