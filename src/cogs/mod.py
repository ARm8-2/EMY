
from utils.checks.checkmute import _checkmute

import discord, asyncio
from discord.ext import commands


class Modcommand(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(name='kick')
    @commands.has_permissions(kick_members=True)
    async def _kick(self, ctx, user: discord.User, *, reason=None):
        embed = discord.Embed(title="User kicked", description="", color=0x161616)
        embed.add_field(name=f"```user:```", value=f"{user}", inline=False)
        embed.add_field(name=f"````reason:````", value=f"{reason}", inline=False)
        await ctx.send(embed=embed)
        embed = discord.Embed(title=f"U have been kicked", description="", color=0x161616)
        embed.add_field(name=f"````reason:````", value=f"{reason}", inline=False)
        await user.send(embed=embed)
        await user.kick(reason=reason)

    @commands.command(name='kickinvite', aliases=['kickinv'])
    @commands.has_permissions(kick_members=True)
    async def _kickinvite(self, ctx, user: discord.User, *, reason=None):
        embed = discord.Embed(title="User kicked", description="", color=0x161616)
        embed.add_field(name=f"```user:```", value=f"{user}", inline=False)
        embed.add_field(name=f"````reason:````", value=f"{reason}", inline=False)
        await ctx.send(embed=embed)
        embed = discord.Embed(title=f"U have been kicked", description="", color=0x161616)
        embed.add_field(name=f"````reason:````", value=f"{reason}", inline=False)
        await user.send(embed=embed)
        invitelink = await ctx.channel.create_invite(max_uses=1, unique=True)
        await user.send(invitelink)
        await user.kick(reason=reason)

    @commands.command(name='ban')
    @commands.has_permissions(ban_members=True)
    async def _ban(self, ctx, user: discord.User, *, reason=None):
        embed = discord.Embed(title="User banned", description="", color=0x161616)
        embed.add_field(name=f"```user:```", value=f"{user}", inline=False)
        embed.add_field(name=f"````reason:````", value=f"{reason}", inline=False)
        await ctx.send(embed=embed)
        embed = discord.Embed(title=f"U have been banned", description="", color=0x161616)
        embed.add_field(name=f"````reason:````", value=f"{reason}", inline=False)
        await user.send(embed=embed)
        await user.ban(reason=reason)

    @commands.command(name='unban')
    @commands.has_permissions(ban_members=True)
    async def _unban(self, ctx, *, user):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = user.split('#')
        for ban_entry in banned_users:
            user = ban_entry.user
            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                embed = discord.Embed(title="User unbanned", description="", color=0x161616)
                embed.add_field(name=f"```user:```", value=f"{user}", inline=False)
                await ctx.send(embed=embed)

    @commands.command(name='mute')
    @commands.has_permissions(kick_members=True)
    async def _mute(self, ctx, user: discord.User, *, reason=None):
        await _checkmute(ctx.guild)
        role_muted = discord.utils.get(ctx.guild.roles, name='muted')
        await user.add_roles(role_muted)
        embed = discord.Embed(title="User muted", description="", color=0x161616)
        embed.add_field(name=f"```user:```", value=f"{user}", inline=False)
        embed.add_field(name=f"````reason:````", value=f"{reason}", inline=False)
        await ctx.send(embed=embed)

    @commands.command(name='unmute')
    @commands.has_permissions(kick_members=True)
    async def _unmute(self, ctx, user: discord.User):
        role_muted = discord.utils.get(ctx.guild.roles, name='muted')
        await user.remove_roles(role_muted)
        embed = discord.Embed(title="User unmuted", description="", color=0x161616)
        embed.add_field(name=f"```user:```", value=f"{user}", inline=False)
        await ctx.send(embed=embed)

    @commands.command(name='tempmute')
    @commands.has_permissions(kick_members=True)
    async def _tempmute(self, ctx, user: discord.Member, inputtime, reason=None):
        time_dict = {'s': 1, 'm': 60, 'h': 3600, 'd': 86400, 'w': 604800}
        time = time_dict[inputtime[-1]] * int(inputtime[:-1])
        await _checkmute(ctx.guild)
        role_muted = discord.utils.get(ctx.guild.roles, name='muted')
        await user.add_roles(role_muted)
        embed = discord.Embed(title="User temporarily muted", description="", color=0x161616)
        embed.add_field(name=f"```user:```", value=f"{user}", inline=False)
        embed.add_field(name=f"```time:```", value=inputtime, inline=False)
        embed.add_field(name=f"```reason:```", value=f"{reason}", inline=False)
        await ctx.send(embed=embed)
        await asyncio.sleep(time)
        await user.remove_roles(role_muted)

    @commands.command(name='clear', aliases=['purge'])
    @commands.has_permissions(manage_messages=True)
    async def _clear(self, ctx, amount=1):
        amount += 1
        await ctx.channel.purge(limit=amount)


def setup(client):
    client.add_cog(Modcommand(client))
