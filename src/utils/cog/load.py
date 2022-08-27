
from utils.settings import client
from utils.settings import BASE
from utils.alert import _alert

import os
from discord.ext import commands

async def _loadext(ctx, extension):
    if extension == 'all':
        for filename in os.listdir(os.path.join(BASE, 'src', 'cogs')):
            if filename.endswith('.py'):
                try:
                    client.load_extension(f'cogs.{filename[:-3]}')
                except commands.ExtensionAlreadyLoaded:
                    pass
        await _alert(ctx=None, action='load', data='all')
    else:
        try:
            client.load_extension(f'cogs.{extension}')
        except commands.ExtensionAlreadyLoaded:
            pass
        await _alert(ctx=None, action='load', data=extension)