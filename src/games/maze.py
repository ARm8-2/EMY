
import discord
from discord.ext import commands
from utils.resources import _getmaze
from utils.settings import color


class Maze:
    layout = _getmaze(1)["layout"]
    height = _getmaze(1)["height"]
    
    def render():
        return str(str(Maze.layout).replace("]", "\n").replace("[", "").replace(",", "").replace("\'0\'", ":black_large_square:").replace("\'1\'", ":white_large_square:"))

    def getlayout():
        return Maze.layout



class Player:
    x = _getmaze(1)["startpos"]["x"]
    y = _getmaze(1)["startpos"]["y"]

    def _moveup(self):
        self.y+=1

    def _movedown(self):
        self.y-=1

    def _moveleft(self):
        self.x-=1

    def _moveright(self):
        self.x+=1

async def _maze(ctx: commands.Context):
    embed = discord.Embed(title="**EMY** game", description=Maze.getlayout, color=color)
    await ctx.channel.send(embed=embed)
