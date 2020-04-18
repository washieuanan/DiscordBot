import discord
import random
from discord.ext import commands
import asyncio 
import typing
import os


client = commands.Bot(command_prefix= '$')

@client.event
async def on_ready():
    print('Bot is ready')

@client.event
async def on_member_join(ctx, member):
    print(f'{member} has joined the server.')

@client.event
async def on_member_remove(ctx, member):
    print(f'{member} has left the server.')


@client.command()
async def ping(ctx):
    await ctx.send(f'Your current internet ping is: {round(client.latency * 1000)}ms')

@client.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
    responses = ['It is certain.',
                 'It is decidedly so.',
                 'Without a doubt.',
                 'Yes, definitely.',
                 'You may rely on it.',
                 'As I see it, yes.',
                 'Most likely.',
                 'Outlook good.',
                 'Yes.', 
                 'The signs point towards yes.',
                 'Reply hazy, try again.',
                 'Better not tell you now ;)',
                 'Cannot predict now.',
                 'Concetrate and ask me again!',
                 'Do not count on it.',
                 'My reply is no.',
                 'My sources say no.',
                 'Outlook not so good.',
                 'Very doubtful.']

    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

@client.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)

    if amount == 0:
        await ctx.send('Invalid amount. Please send a valid amount of messages that you would like to delete.')

@client.command()
async def kick(ctx, member : discord.Member = None, *, reason = None):
    await member.kick(reason = reason)
    await ctx.send(f'**{member.display_name}** has been kicked *{reason}*')

    if not member:
        await ctx.send("Please identify the person that you would like to kick.")
        return 

    

@client.command()
async def ban(ctx, member: discord.Member = None, *, reason = None):
    await member.ban(reason = reason)
    await ctx.send(f'**{member.display_name}** has been banned *{reason}*')

    if not member:
        await ctx.send('Please identify the person that you would like to ban. ')
        return


@client.command()
async def warn(ctx, member: discord.Member = None, *, reason = None):
    await ctx.send(f'**{member.display_name}** has been warned *{reason}*')

@client.command()
async def unban(ctx, *, member):
    bannedUsers = await ctx.guild.bans()
    memberName, memberDiscriminator = member.split('#')

    for banEntry in bannedUsers:
        user = banEntry.user

        if(user.name, user.discriminator) == (memberName, memberDiscriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'{user.name}#{user.discriminator} has been unbanned in this server.')

@client.command(pass_context = True)
async def mute(ctx, user, reason):
    role = discord.utils.get(ctx.guild.roles, name="Muted")
    hell = discord.utils.get(ctx.guild.text_channels, name="Hell")
    
    if not role:
        try:
            muted = await ctx.guild.create_role(name="Muted", reason = "To use for muting")
            for channel in ctx.guild.channels:
                await channel.set_permissions(muted, send_messages = False)

        except discord.Forbidden:
            return await ctx.send("I have no permission to mute someone")
        await user.add_roles(muted)
        await ctx.send(f'{user.mention} has been muted for {reason}')
    else:
        await user.add_roles(role)
        await ctx.send(f"{user.mention} has already been muted previously for {reason}")
    
    if not hell: 
        overwrites = {ctx.guild.default_role: discord.PermissionOverwrite(read_message_history = False), 
                      ctx.guild.me: discord.PermissionOverwrite(send_messages = True), 
                      muted: discord.PermissionOverwrite(read_message_history = True)}
        try:
            channel = await ctx.create_channel('Mutes', overwrites = overwrites)
            await channel.send("Welcome to the muted channel.. You will spend your time here until you get unmuted. Enjoy the silence :)")
        except discord.Forbidden:
            return await ctx.send("I have no permission to make this channel")

@client.command()
async def unmute(ctx, user):
    await user.remove_roles(discord.utils.get(ctx.guild.roles, name = "Muted"))
    await ctx.send(f"{user.mention} has been unmuted.")

#Bot Token 
client.run("CANNOT RELEASE BOT TOKEN TO THE PUBLIC")

