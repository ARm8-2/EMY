
import json
import os

from utils.alert import _alert
from utils.settings import BASEDIR, prefix


async def _on_guild_join(guild):
    with open(os.path.join(BASEDIR, 'resources', 'serverdata.json'), 'r') as f:
            data = json.load(f)

    if str(guild.id) not in data:
        data[str(guild.id)] = {}
        data[str(guild.id)]["servername"] = str(guild.name)
        data[str(guild.id)]["prefix"] = prefix
        data[str(guild.id)]["miscchannel"] = []
        data[str(guild.id)]["cooldown"] = []

    with open(os.path.join(BASEDIR, 'resources', 'serverdata.json'), 'w') as f:
        json.dump(data, f, indent=4)

    _alert(action="guildjoined", data=guild)
