
from utils.settings import token
from utils.settings import prefix
from utils.settings import client
from utils.settings import BASE
from utils.cog.load import _loadext
from utils.cog.unload import _unloadext
from utils.cog.reload import _reloadext
from utils.alert import _alert
from events.guild.on_guild_join import _onguildjoin
from events.guild.on_guild_remove import _onguildremove

import discord, logging
from discord.ext import commands


client.remove_command('help')
print(f'INFO:base.directory:{BASE}')
logging.basicConfig(level=logging.INFO)


@client.command(name='load')
@commands.is_owner()
async def _load(ctx, extension):
    await _loadext(ctx, extension)


@client.command(name='unload')
@commands.is_owner()
async def _unload(ctx, extension):
    await _unloadext(ctx, extension)


@client.command(name='reload')
@commands.is_owner()
async def _reload(ctx, extension):
    await _reloadext(ctx, extension)


@client.command(name='shutdown')
@commands.is_owner()
async def _shutdown(ctx=None):
    await _alert(ctx=None, action='shutdown')
    exit()


@client.event
async def on_guild_join(guild):
    await _onguildjoin(guild)


@client.event
async def on_guild_remove(guild):
    await _onguildremove(guild)


@client.event
async def on_ready():
    await _reloadext(ctx=None, extension='all')
    await client.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.listening, name=f"{prefix}help"))
    print('Logged in as:\n{0.user.name}\n{0.user.id}'.format(client))


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument) or isinstance(error, commands.MissingPermissions):
        await ctx.send('An error occurred: {}'.format(str(error)))


client.run(token)
