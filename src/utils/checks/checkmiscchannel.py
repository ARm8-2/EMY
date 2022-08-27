
import json
import os

from utils.settings import BASEDIR


def _checkmiscchannel(ctx):
    if ctx.guild==None:
        return True
    else:
        with open(os.path.join(BASEDIR, 'resources', 'serverdata.json'), 'r') as f:
            data = json.load(f)
        return ctx.channel.id in data[str(ctx.guild.id)]["miscchannel"]
