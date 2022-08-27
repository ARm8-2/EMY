
from utils.settings import BASE

import json, os

async def _checkservername(guild):
    with open(os.path.join(BASE, 'resources', 'serverdata.json'), 'r') as f:
        data = json.load(f)

    data[str(guild.id)]["servername"] = str(guild.name)

    with open(os.path.join(BASE, 'resources', 'serverdata.json'), 'w') as f:
        json.dump(data, f, indent=4)