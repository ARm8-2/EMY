
import json
import discord
import os
from discord.ext import commands

BASE = os.getcwd()
if BASE.endswith('src'):
    n = BASE.rfind("\\")
    BASE = BASE[0: n+1]

with open(os.path.join(BASE, 'src', 'settings', 'config.json'), 'r') as f:
    data = json.load(f)
    token = data["token"]
    prefix = data["prefix"]
    ownerid = data["ownerid"]
    color = int(data["color"], 16)

def _getprefix(client, ctx):
    with open(os.path.join(BASE, 'resources', 'serverdata.json'), 'r') as f:
        data = json.load(f)

    if ctx.guild is None:
        return prefix
    else:
        return data[str(ctx.guild.id)]["prefix"]


client = commands.Bot(command_prefix=_getprefix, intents = discord.Intents.all())
