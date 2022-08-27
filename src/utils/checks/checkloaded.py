
import os

from discord.ext import commands
from utils.alert import _alert
from utils.settings import BASEDIR, client


async def _checkloadedext(ctx, extension=None):
    dir = {'loaded': [], 'notloaded':  []}

    if extension=='all' or extension==None:
        for filename in os.listdir(os.path.join(BASEDIR, 'src', 'cogs')):
            if filename.endswith('.py'):
                try:
                    client.load_extension(f'cogs.{filename[:-3]}')
                    dir['notloaded'].append(filename)
                except commands.ExtensionAlreadyLoaded:
                    dir['loaded'].append(filename)
        await _alert(ctx=None, action="checkloaded", data=dir)
    else:
        try:
            client.load_extension(f'cogs.{extension}')
            dir['notloaded'].append(filename)
        except commands.ExtensionAlreadyLoaded:
            dir['loaded'].append(filename)
        await _alert(ctx=None, action="checkloaded", data=dir)
