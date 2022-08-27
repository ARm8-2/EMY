
from utils.settings import client
from utils.settings import BASE
from utils.alert import _alert

import os
from discord.ext import commands


async def _reloadext(ctx, extension):
    if extension == 'all':
        for file in os.listdir(os.path.join(BASE, 'src', 'cogs')):
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