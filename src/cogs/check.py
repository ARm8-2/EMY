
import discord
from discord.ext import commands


class Check(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(name='check')
    async def _check(self, ctx):
        pass

def setup(client):
    client.add_cog(Check(client))
