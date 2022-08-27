
import json
import os

from discord.ext import commands
from utils.settings import BASEDIR


def _checkmiscchannel(ctx: commands.Context):
    if ctx.guild==None:
        return True
    else:
        with open(os.path.join(BASEDIR, 'resources', 'serverdata.json'), 'r') as f:
            data = json.load(f)
        return ctx.channel.id in data[str(ctx.guild.id)]["miscchannel"]
