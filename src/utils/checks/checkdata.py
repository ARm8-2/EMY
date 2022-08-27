
from utils.checks.checkloaded import _checkloadedext
from utils.checks.checkservername import _checkservername
from utils.settings import client


async def _checkdata():
    await _checkloadedext(ctx=None, extension='all')
    await _checkservername(guild='all')
