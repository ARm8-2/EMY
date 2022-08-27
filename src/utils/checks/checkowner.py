
from utils.settings import ownerid


async def _checkowner(user):
    if user.id == ownerid:
        return True
    else:
        return False
