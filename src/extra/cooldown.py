
from utils.checks.checkmute import _checkmute
from utils.settings import color

import asyncio, discord, json
from discord.ext import commands


class Cooldown(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(name='cooldown', aliases=['cd'])
    @commands.has_permissions(kick_members=True)
    async def _cooldown(self, ctx, action, user: discord.Member, *, reason=None):
        if action == 'add':
            with open('./resources/serverdata.json', 'r') as f:
                data = json.load(f)

            if user.id not in data[str(ctx.guild.id)]["cooldown"]:
                data[str(ctx.guild.id)]["cooldown"].append(user.id)
                embed = discord.Embed(title="Added cooldown", description="", color=color)
                embed.add_field(name=f"```user:```", value=f"{user}", inline=False)
                embed.add_field(name=f"````reason:````", value=f"{reason}", inline=False)
                await ctx.send(embed=embed)
            elif user.id in data[str(ctx.guild.id)]["cooldown"]:
                embed = discord.Embed(title="User already has a cooldown", description="", color=color)
                embed.add_field(name=f"```user:```", value=f"{user}", inline=False)
                await ctx.send(embed=embed)

            with open('./resources/serverdata.json', 'w') as f:
                json.dump(data, f, indent=4)
        
        if action == 'remove':
            with open('./resources/serverdata.json', 'r') as f:
                data = json.load(f)

            try:
                data[str(ctx.guild.id)]["cooldown"].remove(user.id)
                embed = discord.Embed(title="Removed cooldown", description="", color=color)
                embed.add_field(name=f"```user:```", value=f"{user}", inline=False)
                await ctx.send(embed=embed)
            except user.id not in data[str(ctx.guild.id)]["cooldown"]:
                embed = discord.Embed(title="User does not have a cooldown", description="", color=color)
                embed.add_field(name=f"```user:```", value=f"{user}", inline=False)
                await ctx.send(embed=embed)

            with open('./resources/serverdata.json', 'w') as f:
                json.dump(data, f, indent=4)

    @commands.Cog.listener()
    async def on_message(self, ctx):
        if ctx.channel == None:
            return
        else:
            with open("./resources/serverdata.json", "r") as f:
                data = json.load(f)
                try:
                    if ctx.author.id != "847505802616897587" and ctx.author.id in data[str(ctx.guild.id)]["cooldown"]:
                        await _checkmute(ctx.guild)
                        role_muted = discord.utils.get(ctx.guild.roles, name='muted')
                        await ctx.author.add_roles(role_muted)
                        await asyncio.sleep(10)
                        await ctx.author.remove_roles(role_muted)
                except:
                    pass


def setup(client):
    client.add_cog(Cooldown(client))