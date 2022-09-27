
from discord.ext import commands

from games.maze import _maze


class Games(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(name='game', aliases=['playgame'])
    async def _game(self, ctx: commands.Context, game):
        if game=='maze':
            await _maze(ctx=ctx)

def setup(client):
    client.add_cog(Games(client))
