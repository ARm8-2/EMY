
from utils.settings import color
from utils.settings import _getprefix

import discord
from discord.ext import commands


class Help(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(name='help')
    async def _help(self, ctx):
        embed = discord.Embed(title="**EMY** help",
                              description=f'\n`< >` - required argument'
                                          f'\n`[ ]` - non-required argument'

                                          f'\n'

                                          f'\n`{_getprefix(self, ctx)}abbreviations` - shows abbreviations for commands'
                                          f'\n`{_getprefix(self, ctx)}info` - shows info about the bot'
                                          f'\n`{_getprefix(self, ctx)}modhelp` - help for moderating'
                                          f'\n`{_getprefix(self, ctx)}ping` - shows the bot latency'

                                          f'\n\n __miscellaneous__:\n'
                                          f'\n`{_getprefix(self, ctx)}8ball <question>` - answers your question'
                                          f'\n`{_getprefix(self, ctx)}avatar [user]` - shows a large version of the users avatar'
                                          f'\n`{_getprefix(self, ctx)}coinflip` - flips a coin'
                                          f'\n`{_getprefix(self, ctx)}embed <message>` - let\'s the bot say your message as an embed'
                                          f'\n`{_getprefix(self, ctx)}fps [user]` - shows the fps of the user'
                                          f'\n`{_getprefix(self, ctx)}meme` - shows a meme'
                                          f'\n`{_getprefix(self, ctx)}pun` - shows a pun'
                                          f'\n`{_getprefix(self, ctx)}say <message>` - let\'s the bot say your message'

                                          f'\n\n __music__:\n'
                                          f'\n`{_getprefix(self, ctx)}forceskip` - skips the current song'
                                          f'\n`{_getprefix(self, ctx)}join` - joins voicechannel'
                                          f'\n`{_getprefix(self, ctx)}leave` - leaves voicechannel'
                                          f'\n`{_getprefix(self, ctx)}loop` - loops current song'
                                          f'\n`{_getprefix(self, ctx)}now` - shows current song'
                                          f'\n`{_getprefix(self, ctx)}pause` - pauses current song'
                                          f'\n`{_getprefix(self, ctx)}play <song>` - plays song'
                                          f'\n`{_getprefix(self, ctx)}queue` - shows the current queue'
                                          f'\n`{_getprefix(self, ctx)}remove <index>` - removes a song from the queue'
                                          f'\n`{_getprefix(self, ctx)}resume` - resumes the queue'
                                          f'\n`{_getprefix(self, ctx)}search <song>` - searhes for song and shows 10 results'
                                          f'\n`{_getprefix(self, ctx)}shuffle` - shuffles the current queue'
                                          f'\n`{_getprefix(self, ctx)}skip` - skips the current'
                                          f'\n`{_getprefix(self, ctx)}stop` - stops the song and clear the queue'
                                          f'\n`{_getprefix(self, ctx)}summon [channel]` - summons the bot to a channel',
                              color=color)
        await ctx.message.add_reaction('✅')
        await ctx.author.send(embed=embed)

    @commands.command(name='modhelp')
    async def _modhelp(self, ctx):
        embed = discord.Embed(title="**EMY** modhelp",
                              description=f'\n`< >` - required argument'
                                          f'\n`[ ]` - non-required argument'

                                          f'\n'

                                          f'\n`{_getprefix(self, ctx)}changeprefix <prefix>` - changes the prefix'
                                          f'\n`{_getprefix(self, ctx)}misccommand [channel]` - enables/disables miscellaneous commands in a channel'
                                          f'\n`{_getprefix(self, ctx)}permissions` - shows needed permissions'

                                          f'\n\n __moderating__:\n'
                                          f'\n`{_getprefix(self, ctx)}ban <user> [reason]` - bans user'
                                          f'\n`{_getprefix(self, ctx)}clear <amount>` - deletes amount of messages'
                                          f'\n`{_getprefix(self, ctx)}cooldown <add|remove> <user> [reason]` - add\'s/removes a cooldown for a specific user'
                                          f'\n`{_getprefix(self, ctx)}kick <user> [reason]` - kick user'
                                          f'\n`{_getprefix(self, ctx)}kickinvite <user> [reason]` - kick user and send invite'
                                          f'\n`{_getprefix(self, ctx)}mute <user> [reason]` - mutes user'
                                          f'\n`{_getprefix(self, ctx)}tempmute <user> <time> [reason]` - temporarily mutes user'
                                          f'\n`{_getprefix(self, ctx)}unban <user> [reason]` - unbans user'
                                          f'\n`{_getprefix(self, ctx)}unmute <user>` - unmutes user',
                              color=color)
        await ctx.message.add_reaction('✅')
        await ctx.author.send(embed=embed)

    @commands.command(name='info')
    async def _info(self, ctx):
        embed = discord.Embed(title="**EMY** info",
                              description=f'Hi, i am EMY, a special ai bot that can help you with many things.\nI am still being developed and can not help with everything yet.'
                                          f'\nIf you have any problems please check {_getprefix(self, ctx)}help and {_getprefix(self, ctx)}faq before sending a dm.',
                              color=color)
        await ctx.message.add_reaction('✅')
        await ctx.author.send(embed=embed)

    @commands.command(name='faq')
    async def _faq(self, ctx):
        embed = discord.Embed(title="**EMY** FAQ",
                              description=f'Here are the most frequently asked question.',
                              color=color)
        embed.add_field(name='\nThe miscellaneous commands aren\'t working',
                        value=f'enable miscellaneous commands by doing {_getprefix(self, ctx)}misccommand ({_getprefix(self, ctx)}modhelp)', inline=False)
        embed.add_field(name='\nThe music doesn\'t play',
                        value=f'This is a bug, you can do {_getprefix(self, ctx)}disconnect to fix the problem', inline=False)
        embed.add_field(name='\nThe bot\'s automoderating is not working',
                        value=f'Check the permissions of the bot, you can find the permissions the bot needs with {_getprefix(self, ctx)}permissions', inline=False)
        await ctx.message.add_reaction('✅')
        await ctx.author.send(embed=embed)

    @commands.command(name='permissions', aliases=['perms', 'perm'])
    async def _permissions(self, ctx):
        embed = discord.Embed(title="**EMY** permissions",
                              description=f'The bot doesn\'t need all permissions but not all commands will work if it doesn\'t have the right permissions\n'
                                          f'\nGENERAL SERVER PERMISSIONS\n'
                                          f'\nView Channels'
                                          f'\nManage Channels'
                                          f'\nManage Roles'
                                          f'\nManage Emojis'
                                          f'\n\nMEMBERSHIP PERMISSIONS\n'
                                          f'\nCreate Invite'
                                          f'\nKick Members'
                                          f'\nBan Members'
                                          f'\n\nTEXT CHANNEL PERMISSIONS\n'
                                          f'\nSend Messages'
                                          f'\nEmbed Links'
                                          f'\nAttach Files'
                                          f'\nAdd Reactions'
                                          f'\nMention @everyone, @here and All RRoles'
                                          f'\nManage Messages'
                                          f'\n\nVOICE CHANNEL PERMISSIONS\n'
                                          f'\nConnect'
                                          f'\nSpeak',
                              color=color)
        await ctx.message.add_reaction('✅')
        await ctx.author.send(embed=embed)

    @commands.command(name='abbreviations', aliases=['abb'])
    async def _abbreviations(self, ctx):
        embed = discord.Embed(title="**EMY** abbreviations",
                              description=f'\n**help**\n'
                                          f'\n`{_getprefix(self, ctx)}abbreviations - {_getprefix(self, ctx)}abb`'

                                          f'\n\n __chat__:\n'
                                          f'\n`{_getprefix(self, ctx)}avatar [user] - {_getprefix(self, ctx)}av [user]`'

                                          f'\n\n __music__:\n'
                                          f'\n`{_getprefix(self, ctx)}forceskip - {_getprefix(self, ctx)}fs`'
                                          f'\n`{_getprefix(self, ctx)}join - {_getprefix(self, ctx)}j`'
                                          f'\n`{_getprefix(self, ctx)}leave - {_getprefix(self, ctx)}l`'
                                          f'\n`{_getprefix(self, ctx)}now - {_getprefix(self, ctx)}np`'
                                          f'\n`{_getprefix(self, ctx)}pause - {_getprefix(self, ctx)}pa`'
                                          f'\n`{_getprefix(self, ctx)}play <song> - {_getprefix(self, ctx)}p <song>`'
                                          f'\n`{_getprefix(self, ctx)}queue - {_getprefix(self, ctx)}q`'
                                          f'\n`{_getprefix(self, ctx)}remove <index> - {_getprefix(self, ctx)}rem <index>`'
                                          f'\n`{_getprefix(self, ctx)}resume - {_getprefix(self, ctx)}res`'
                                          f'\n`{_getprefix(self, ctx)}skip - {_getprefix(self, ctx)}s`'

                                          f'\n\n**modhelp**\n'

                                          f'\n`{_getprefix(self, ctx)}changeprefix <prefix> - prefix <prefix>`'
                                          f'\n`{_getprefix(self, ctx)}funchannel [channel] - cc [channel]`'
                                          f'\n`{_getprefix(self, ctx)}permissions - perms`'

                                          f'\n\n __moderating__:\n'
                                          f'\n`{_getprefix(self, ctx)}kickinvite <user> [reason] - {_getprefix(self, ctx)}kickinv <user> [reason]`',
                              color=color)
        await ctx.message.add_reaction('✅')
        await ctx.author.send(embed=embed)


def setup(client):
    client.add_cog(Help(client))
