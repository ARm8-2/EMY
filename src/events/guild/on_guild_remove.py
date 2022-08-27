
import json
import os

from utils.alert import _alert
from utils.settings import BASEDIR


async def _on_guild_remove(guild):
    with open(os.path.join(BASEDIR, 'resources', 'serverdata.json'), 'r') as f:
        data = json.load(f)

    data.pop(str(guild.id))

    with open(os.path.join(BASEDIR, 'resources', 'serverdata.json'), 'w') as f:
        json.dump(data, f, indent=4)

    _alert(action="guildremoved", data=guild)
