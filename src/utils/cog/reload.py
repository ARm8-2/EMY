
import os

from discord.ext import commands
from utils.alert import _alert
from utils.settings import BASEDIR, client


async def _reload(ctx: commands.Context, extension):
    if extension == 'all':
        for file in os.listdir(os.path.join(BASEDIR, 'src', 'cogs')):
            if file.endswith('.py'):
                try:
                    client.unload_extension(f'cogs.{file[:-3]}')
                    client.load_extension(f'cogs.{file[:-3]}')
                except commands.ExtensionNotLoaded:
                    client.load_extension(f'cogs.{file[:-3]}')
        await _alert(ctx=None, action='reload', data='all')
    else:
        try:
            client.unload_extension(f'cogs.{extension}')
            client.load_extension(f'cogs.{extension}')
        except commands.ExtensionNotLoaded:
            client.load_extension(f'cogs.{extension}')
        await _alert(ctx=None, action='reload', data=extension)
