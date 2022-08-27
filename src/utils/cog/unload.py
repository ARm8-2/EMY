
import os

from discord.ext import commands
from utils.alert import _alert
from utils.settings import BASEDIR, client


async def _unload(ctx, extension):
    if extension == 'all':
        for filename in os.listdir(os.path.join(BASEDIR, 'src', 'cogs')):
            if filename.endswith('.py'):
                try:
                    client.unload_extension(f'cogs.{filename[:-3]}')
                except commands.ExtensionNotLoaded:
                    pass
        await _alert(ctx=None, action='unload', data='all')
    else:
        try:
            client.unload_extension(f'cogs.{extension}')
        except commands.ExtensionNotLoaded:
            pass
        await _alert(ctx=None, action='unload', data=extension)
