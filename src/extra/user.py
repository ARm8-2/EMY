
from utils.settings import color
from utils.checks.checkmute import _checkmute

import discord
from discord_components import *
from discord.ext import commands


class User(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(name='user')
    async def _user(self, ctx, user: discord.User):
        avatar = user.avatar_url
        embed = discord.Embed(title='', description='', color=color)
        embed.set_author(name=user.name, icon_url=avatar)
        await ctx.send(embed=embed, components = [ActionRow(
            Button(label='mute', style=ButtonStyle.gray, custom_id=f'mute;{str(user.id)}'), 
            Button(label='unmute', style=ButtonStyle.gray, custom_id=f'unmute;{str(user.id)}'), 
            Button(label='kick', style=ButtonStyle.gray, custom_id=f'kick;{str(user.id)}'),
            Button(label='invitekick', style=ButtonStyle.gray, custom_id=f'invitekick;{str(user.id)}')),
            ActionRow(
            Button(label='ban', style=ButtonStyle.gray, custom_id=f'ban;{str(user.id)}'), 
            Button(label='unban', style=ButtonStyle.gray, custom_id=f'unban;{str(user.id)}')
            )])
        

    @commands.Cog.listener()
    async def on_button_click(self, interaction):

        if interaction.component.label == 'mute':
            userid = int(interaction.component.custom_id.split(';')[1])
            user = await interaction.guild.fetch_member(userid)

            await _checkmute(interaction.guild)
            role_muted = discord.utils.get(interaction.guild.roles, name='muted')
            await user.add_roles(role_muted)
            
            await interaction.message.edit(components = [ActionRow(
                Button(label='mute', style=ButtonStyle.green, custom_id=f'mute;{str(user.id)}', disabled=True), 
                Button(label='unmute', style=ButtonStyle.gray, custom_id=f'unmute;{str(user.id)}'), 
                Button(label='kick', style=ButtonStyle.gray, custom_id=f'kick;{str(user.id)}'),
                Button(label='invitekick', style=ButtonStyle.gray, custom_id=f'invitekick;{str(user.id)}')   
                )])
            await interaction.respond(content=f'muted {user}')

        if interaction.component.label == 'unmute':
            userid = int(interaction.component.custom_id.split(';')[1])
            user = await interaction.guild.fetch_member(userid)

            await _checkmute(interaction.guild)
            role_muted = discord.utils.get(interaction.guild.roles, name='muted')
            await user.remove_roles(role_muted)
            
            await interaction.message.edit(components = [ActionRow(
                Button(label='mute', style=ButtonStyle.gray, custom_id=f'mute;{str(user.id)}'), 
                Button(label='unmute', style=ButtonStyle.green, custom_id=f'unmute;{str(user.id)}', disabled=True), 
                Button(label='kick', style=ButtonStyle.gray, custom_id=f'kick;{str(user.id)}'),
                Button(label='invitekick', style=ButtonStyle.gray, custom_id=f'invitekick;{str(user.id)}'))])
            await interaction.respond(content=f'unmuted {user}')


def setup(client):
    client.add_cog(User(client))