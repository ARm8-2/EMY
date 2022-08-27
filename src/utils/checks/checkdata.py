
from utils.checks.checkloaded import _checkloadedext
from utils.checks.checkservername import _checkservername
from utils.settings import client

datachecks = False

def _datacheck():
    if datachecks:
        datachecks = False
    else:
        datachecks = True

async def check():
    while datachecks:
        await _checkloadedext(ctx=None, extension='all')
        await _checkservername(guild='all')
