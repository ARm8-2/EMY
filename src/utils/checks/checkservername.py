
import json
import os

from utils.settings import BASEDIR


async def _checkservername(guild):
    with open(os.path.join(BASEDIR, 'resources', 'serverdata.json'), 'r') as f:
        data = json.load(f)

    data[str(guild.id)]["servername"] = str(guild.name)

    with open(os.path.join(BASEDIR, 'resources', 'serverdata.json'), 'w') as f:
        json.dump(data, f, indent=4)
