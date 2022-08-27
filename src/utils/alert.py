
import discord

from utils.settings import client, color, ownerid


async def _alert(ctx, action, data=None):
    embed = discord.Embed(title="ALERT", color=color)

    if action=='shutdown':
        description = f"Shutting down..."

    if action=='load':
        description = f"Loaded {data}.py"

    if action=='load' and data=='all':
        description = f"Loaded all cogs"

    if action=='unload':
        description = f"Unloaded {data}.py"

    if action=='unload' and data=='all':
        description = f"Unloaded all cogs"

    if action=='reload':
        description = f"Reloaded {data}.py"

    if action=='reload' and data=='all':
        description = f"Reloaded all cogs"

    if action=='checkloaded':
        description='Checked for unloaded cogs'
        embed.add_field(name="Loaded", value=str(data["loaded"]))
        embed.add_field(name="Not loaded", value=str(data["notloaded"]), inline=False)

    if action=='guildjoined':
        description = f"EMY joined new server: {data}"

    if action=='guildremoved':
        description = f"EMY removed from server: {data}"

    embed.description = description

    if ctx==None:
        await client.get_user(ownerid).send(embed=embed)
    else:
        try:
            await ctx.send(embed=embed)
        except:
            pass

    print(f"[ALERT] {description}")
