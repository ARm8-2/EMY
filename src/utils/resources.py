
from utils.settings import color
from utils.settings import BASE

import json, os
import discord


async def _changeprefix(ctx, prefix):
    with open(os.path.join(BASE, 'resources', 'serverdata.json'), 'r') as f:
        data = json.load(f)

    data[str(ctx.guild.id)]["prefix"] = prefix

    with open(os.path.join(BASE, 'resources', 'serverdata.json'), 'w') as f:
        json.dump(data, f, indent=4)

    embed = discord.Embed(title="", description=f"Prefix changed to {prefix}", color=color)
    await ctx.send(embed=embed)

async def _miscchannel(ctx, channel: discord.TextChannel=None):
    with open(os.path.join(BASE, 'resources', 'serverdata.json'), 'r') as f:
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

    with open(os.path.join(BASE, 'resources', 'serverdata.json'), 'w') as f:
        json.dump(data, f, indent=4)


def _getpuns():
    with open(os.path.join(BASE, 'resources', 'serverdata.json'), 'r', encoding="utf8") as f:
        data = json.load(f)

    return data["puns"]
    