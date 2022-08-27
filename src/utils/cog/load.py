
import os

from discord.ext import commands
from utils.alert import _alert
from utils.settings import BASEDIR, client


async def _load(ctx: commands.Context, extension):
    if extension == 'all':
        for filename in os.listdir(os.path.join(BASEDIR, 'src', 'cogs')):
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
