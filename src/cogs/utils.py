
import discord
from discord.ext import commands

from utils.resources import _changeprefix, _miscchannel


class Utils(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(name='changeprefix', aliases=['prefix'])
    async def _changeprefic(self, ctx: commands.Context, prefix):
        await _changeprefix(ctx=ctx, prefix=prefix)

    @commands.command(name='misccchannel')
    async def _miscchannel(self, ctx: commands.Context, channel: discord.TextChannel=None):
        await _miscchannel(ctx=ctx, channel=channel)

def setup(client):
    client.add_cog(Utils(client))
