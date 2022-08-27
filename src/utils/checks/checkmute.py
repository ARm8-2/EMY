
import discord


async def _checkmute(guild):
    if not discord.utils.get(guild.roles, name="muted"):
        await guild.create_role(name="muted", colour=discord.Colour(0x8c8c8c))
    role_muted = discord.utils.get(guild.roles, name='muted')
    for channel in guild.text_channels:
        await channel.set_permissions(role_muted, send_messages=False)
