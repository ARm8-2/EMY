
from utils.settings import client
from utils.checks.checkloaded import _checkloadedext
from utils.checks.checkservername import _checkservername


datachecks = False

def _datacheck():
    if datachecks:
        datachecks = False
    else:
        datachecks = True

async def check():
    while datachecks:
        await _checkloadedext(ctx=None, extension='all')
        for guild in client.guilds:
            _checkservername(guild)