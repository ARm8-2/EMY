
from utils.settings import BASE

import json, os

def _checkmiscchannel(ctx):
    if ctx.guild==None:
        return True
    else:
        with open(os.path.join(BASE, 'resources', 'serverdata.json'), 'r') as f:
            data = json.load(f)
        return ctx.channel.id in data[str(ctx.guild.id)]["miscchannel"]