
from utils.settings import color
from utils.checks.checkmute import _checkmute

import discord
from discord_components import *
from discord.ext import commands


class User(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(name='help')
    async def _user(self, ctx):
        embed = discord.Embed(title='help', description='', color=color)
        await ctx.send(embed=embed, components = [ActionRow(
            Button(label='help', style=ButtonStyle.green, custom_id=f'help'), 
            Button(label='info', style=ButtonStyle.blue, custom_id=f'info'), 
            Button(label='faq', style=ButtonStyle.red, custom_id=f'faq'),
            Button(label='commands', style=ButtonStyle.gray, custom_id=f'commands')
            )])
        

    @commands.Cog.listener()
    async def on_button_click(self, interaction):

        if interaction.component.label == 'help':
            await interaction.respond(content=help)

        if interaction.component.label == 'info':
            infomsg = f''
            await interaction.respond(content=infomsg)


def setup(client):
    client.add_cog(User(client))