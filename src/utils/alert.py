
import json
import os

import discord

from utils.settings import BASEDIR, client, color, ownerid


async def _alert(ctx, action, data=None):
    embed = discord.Embed(title="ALERT", color=color)

    with open(os.path.join(BASEDIR, 'resources', 'alerts.json'), 'r') as f:
        descriptions = json.load(f)

    description = descriptions[action]

    if action=="load" or action=="reload" or action=="unload":
        if data!='all':
            description.replace({data}, f'{data}.py')
        elif data=='all':
            description.replace({data}, f'all cogs')

    if action=='checkloaded':
        embed.add_field(name="Loaded", value=str(data["loaded"]))
        embed.add_field(name="Not loaded", value=str(data["notloaded"]), inline=False)

    embed.description = description

    if ctx==None:
        await client.get_user(ownerid).send(embed=embed)
    else:
        try:
            await ctx.send(embed=embed)
        except:
            pass

    print(f"[ALERT] {description}")
