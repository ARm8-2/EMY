
from commands.help import _help
from discord.ext import commands


class Help(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(name='help')
    async def _help(self, ctx):
        await _help(self, ctx)

def setup(client):
    client.add_cog(Help(client))
