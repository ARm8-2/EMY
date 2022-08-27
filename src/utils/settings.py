
import json
import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

token = os.getenv('TOKEN')

BASEDIR = os.getcwd()
if BASEDIR.endswith('src'):
    n = BASEDIR.rfind("\\")
    BASEDIR = BASEDIR[0: n+1]

with open(os.path.join(BASEDIR, 'src', 'settings', 'config.json'), 'r') as f:
    data = json.load(f)
    if data["token"]:
        token = data["token"]
    else:
        token = os.getenv('TOKEN')
    prefix = data["prefix"]
    ownerid = data["ownerid"]
    color = int(data["color"], 16)

def _getprefix(client, ctx: commands.Context):
    with open(os.path.join(BASEDIR, 'resources', 'serverdata.json'), 'r') as f:
        data = json.load(f)

    if ctx.guild is None:
        return prefix
    else:
        return data[str(ctx.guild.id)]["prefix"]


client = commands.Bot(command_prefix=_getprefix, intents = discord.Intents.all())
