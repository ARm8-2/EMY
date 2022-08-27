
from utils.settings import client
from utils.settings import BASE
from utils.alert import _alert

import os
from discord.ext import commands

async def _unloadext(ctx, extension):
    if extension == 'all':
        for filename in os.listdir(os.path.join(BASE, 'src', 'cogs')):
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