
from utils.settings import BASE
from utils.alert import _alert

import json, os


async def _onguildremove(guild):
    with open(os.path.join(BASE, 'resources', 'serverdata.json'), 'r') as f:
        data = json.load(f)

    data.pop(str(guild.id))

    with open(os.path.join(BASE, 'resources', 'serverdata.json'), 'w') as f:
        json.dump(data, f, indent=4)

    _alert(action="guildremoved", data=guild)