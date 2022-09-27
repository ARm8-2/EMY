
import json
import os
import random

import discord
from discord.ext import commands

from utils.settings import BASEDIR, color


async def _changeprefix(ctx: commands.Context, prefix):
    with open(os.path.join(BASEDIR, 'resources', 'serverdata.json'), 'r') as f:
        data = json.load(f)

    data[str(ctx.guild.id)]["prefix"] = prefix

    with open(os.path.join(BASEDIR, 'resources', 'serverdata.json'), 'w') as f:
        json.dump(data, f, indent=4)

    embed = discord.Embed(title="", description=f"Prefix changed to {prefix}", color=color)
    await ctx.send(embed=embed)

async def _miscchannel(ctx: commands.Context, channel: discord.TextChannel=None):
    with open(os.path.join(BASEDIR, 'resources', 'serverdata.json'), 'r') as f:
        data = json.load(f)

    if channel == None:
        channel = ctx.channel

    if ctx.channel.id not in data[str(ctx.guild.id)]["miscchannel"]:
        data[str(ctx.guild.id)]["miscchannel"].append(channel.id)
        embed = discord.Embed(title=f"Enabled commands in {channel}", color=color)
        await ctx.send(embed=embed)
    elif channel.id in data[str(ctx.guild.id)]["miscchannel"]:
        data[str(ctx.guild.id)]["miscchannel"].remove(channel.id)
        embed = discord.Embed(title=f"Disabled commands in {channel}", color=color)
        await ctx.send(embed=embed)

    with open(os.path.join(BASEDIR, 'resources', 'serverdata.json'), 'w') as f:
        json.dump(data, f, indent=4)


def _getpuns():
    with open(os.path.join(BASEDIR, 'resources', 'serverdata.json'), 'r', encoding="utf8") as f:
        data = json.load(f)

    return data["puns"]
    
def _getdescriptions(key):
    with open(os.path.join(BASEDIR, 'resources', 'descriptions.json'), 'r', encoding="utf8") as f:
        data = json.load(f)

    return data[key]

def _getmaze(key:int):
    with open(os.path.join(BASEDIR, 'resources', 'games.json'), 'r', encoding="utf8") as f:
        data = json.load(f)
    if key==0:
        return data["mazes"][str(random.randint(1, 5))]
    else:
        return data["mazes"][str(key)]
        