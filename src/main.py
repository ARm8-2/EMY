
import logging

import discord
from discord.ext import commands

from events.guild.on_guild_join import _on_guild_join
from events.guild.on_guild_remove import _on_guild_remove
from utils.checks.checkdata import _checkdata
from utils.cog.load import _load
from utils.cog.reload import _reload
from utils.cog.unload import _unload
from utils.settings import client, prefix, token

client.remove_command('help')
logging.basicConfig(level=logging.INFO)

@client.command()
async def load(ctx: commands.Context, extension):
    await _load(ctx=ctx, extension=extension)

@client.command()
async def reload(ctx: commands.Context, extension):
    await _reload(ctx=ctx, extension=extension)

@client.command()
async def unload(ctx: commands.Context, extension):
    await _unload(ctx=ctx, extension=extension)

@client.event
async def on_guild_join(guild):
    await _on_guild_join(guild=guild)

@client.event
async def on_guild_remove(guild):
    await _on_guild_remove(guild=guild)

@client.event
async def on_ready():
    await _reload(ctx=None, extension='all')
    await _checkdata()
    await client.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.listening, name=f"{prefix}help"))
    print('Logged in as:\n{0.user.name}\n{0.user.id}'.format(client))

@client.event
async def on_command_error(ctx: commands.Context, error):
    if isinstance(error, commands.MissingRequiredArgument) or isinstance(error, commands.MissingPermissions):
        await ctx.send('An error occurred: {}'.format(str(error)))


client.run(token)
