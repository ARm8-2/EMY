
from utils.checks.checkmute import _checkmute

import asyncio
import discord
from discord.ext import commands


class Antispam(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        while True:
            await asyncio.sleep(10)
            with open("./resources/spamdetect.txt", "r+") as file:
                file.truncate(0)

    @commands.Cog.listener()
    async def on_message(self, message):
        counter = 0
    
        with open("./resources/spamdetect.txt", "r+") as file:
            for lines2 in file:
                if lines2.strip("\n") == str(message.author.id):
                    counter += 1

            file.writelines(f"{str(message.author.id)}\n")
            if counter > 5:
                await _checkmute(message)
                role_muted = discord.utils.get(message.guild.roles, name='muted')
                await message.author.add_roles(role_muted)
                embed = discord.Embed(title=f"User muted", description="", color=0xBF1A1A)
                embed.add_field(name=f"```user:```", value=f"{message.author.name}", inline=False)
                embed.add_field(name=f"```duration:```", value=f" 60 seconds", inline=False)
                embed.add_field(name=f"```reason:```", value=f" spamming", inline=False)
                await message.author.send(embed=embed)
                file.truncate(0)
                await asyncio.sleep(60)
                await message.author.remove_roles(role_muted)


def setup(client):
    client.add_cog(Antispam(client))
