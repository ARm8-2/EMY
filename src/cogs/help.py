
from commands.help.help import _help
from discord.ext import commands


class Help(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(name='help')
    async def _help(self, ctx: commands.Context):
        await _help(ctx=ctx)

def setup(client):
    client.add_cog(Help(client))
