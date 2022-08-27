
from utils.settings import color
from utils.resources import _miscchannel
from utils.checks.checkmiscchannel import _checkmiscchannel
from utils.resources import _getpuns

import random, aiohttp, discord
from discord.ext import commands


class Chatcommand(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['misccommandchannel', 'misc'])
    @commands.has_permissions(administrator=True)
    async def miscchannel(self, ctx, channel: discord.TextChannel=None):
        await _miscchannel(ctx, channel)

    @commands.command(pass_context=True, name='meme')
    @commands.check(_checkmiscchannel)
    async def _meme(self, ctx):
        embed = discord.Embed(title="meme", description="", colour=color)

        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://www.reddit.com/r/dankmemes/new.json?sort=hot') as r:
                res = await r.json()
                embed.set_image(url=res['data']['children'][random.randint(0, 25)]['data']['url'])
                await ctx.send(embed=embed)

    @commands.command(name='avatar', aliases=['av'])
    @commands.check(_checkmiscchannel)
    async def _avatar(self, ctx, *, user: discord.User = None):
        if user == None:
            user = ctx.author

        avatar = user.avatar_url
        embed = discord.Embed(title='', description='', color=color)
        embed.set_thumbnail(url=avatar)
        embed.set_author(name=user.name, icon_url=avatar)
        await ctx.send(embed=embed)

    @commands.command(name='pun')
    @commands.check(_checkmiscchannel)
    async def _pun(self, ctx):
        embed = discord.Embed(title=f"pun", description=random.choice(_getpuns()), color=color)
        await ctx.channel.send(embed=embed)

    @commands.command(name='say')
    @commands.check(_checkmiscchannel)
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def _say(self, ctx, *, message):
        await ctx.send(message)
        await ctx.message.delete()

    @commands.command(name='embed')
    @commands.check(_checkmiscchannel)
    async def _embed(self, ctx, *, message):
        embed = discord.Embed(title=f"Message by {ctx.message.author}", description=f'{message}', color=color)
        await ctx.send(embed=embed)
        await ctx.message.delete()

    @commands.command(name='8ball')
    @commands.check(_checkmiscchannel)
    async def _8ball(self, ctx, *, question):
        responses = [
            "It is certain.",
            "It is decidedly so.",
            "Without a doubt.",
            "Yes - definitely.",
            "You may rely on it.",
            "As I see it, yes.",
            "Most likely.",
            "Outlook good.",
            "Yes.",
            "Signs point to yes.",
            "Ask again later.",
            "Better not tell you now.",
            "Cannot predict now.",
            "Don't count on it.",
            "My reply is no.",
            "My sources say no.",
            "Outlook not so good.",
            "Very doubtful"]
        embed = discord.Embed(title=f"8ball", description="", color=color)
        embed.add_field(name=f"```question:```", value=f"{question}", inline=False)
        embed.add_field(name=f"````response:````", value=random.choice(responses), inline=False)
        await ctx.channel.send(embed=embed)

    @commands.command(aliases=['coin', 'flip'])
    @commands.check(_checkmiscchannel)
    async def coinflip(self, ctx):
        randomflip = ['heads', 'tails']
        embed = discord.Embed(title=f"coinflip", description=random.choice(randomflip), color=color)
        await ctx.channel.send(embed=embed)

    @commands.command()
    @commands.check(_checkmiscchannel)
    async def fps(self, ctx, user: discord.Member = None):
        fps = ["has a fps of 5, go buy a new computer instead of this potatoe.",
               "has a fps of 10, turn down your graphics settings or your computer is going to explode.",
               "has a fps of 15, how is your computer this bad.",
               "has a fps of 20, is your monitor from 2000 or what.",
               "has a fps of 30, this seems decent.",
               "has a fps of 43, what kind of random number is that.",
               "has a fps of 60, nice.",
               "has a fps of 75, this is good gaming quality.",
               "has a fps of 120, you got to have a good graphics card and monitor for this.",
               "has a fps of 240, holy shit, your fps is high as f*ck.",
               "has a fps of 480, how.",
               "has a fps of 960, HOW."
               ]
        if user is None:
            user = ctx.author

        embed = discord.Embed(title=f"{user}\'s current fps", description=f"{user} {random.choice(fps)}", color=color)
        await ctx.channel.send(embed=embed)


def setup(client):
    client.add_cog(Chatcommand(client))
