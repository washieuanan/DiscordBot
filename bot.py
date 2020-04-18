import discord
import asyncio
import os
from discord.ext import commands
import random


bot_prefix='$'
client = commands.Bot(command_prefix=bot_prefix)
client.remove_command("help")

@client.event
async def on_ready():
    print("Bot Online")
    print("Name: {}".format(client.user.name))
    print("ID: ()".format(client.user.id))
    await client.change_presence(game=discord.Game(name='type !!help')  ) 
    
@client.event
async def on_command_error(error, ctx):
    if isinstance(error, commands.CommandOnCooldown):
        await client.send_message(ctx.message.channel, content='This command is on a %.2fs cooldown! Please try again later...' % error.retry_after)
    raise error
               
@client.command(pass_context=True)
async def power(ctx):
    """Shows you your hidden abilities!"""

    power = open('./TextFiles/power.txt').read().splitlines()
    power2 = random.choice(power)
    if ctx.message.author.id == "206027308149112832":
        await client.say("<@!206027308149112832> You can fly!")
    else:
        await client.say('%s Your hidden power is: %s' % (ctx.message.author.mention, power2))       
    
@client.command(pass_context=True)
@commands.cooldown(1, 9, commands.BucketType.user)
async def cooldown(ctx):
    """A test command"""

    cooldown = await client.say("Ok. See if this has cooldown now.")

@client.command(pass_context=True)
async def pm(ctx):
    """Private messages you!"""

    await client.send_message(ctx.message.author, "o.o hello there.")

@client.command(pass_context=True)
async def logs(ctx):
    """Recent changes"""

    embed = discord.Embed(title="All the changelogs here!", color=0xE90FF)
    embed.add_field(name="Minor Update!", value="Made help command shorter")
    embed.add_field(name="New Command!", value="Do !!rps and play Rock Paper Scissors with the bot! Added in 17/9/2018.")
    embed.add_field(name="New Command!", value="Do !!casino and try your luck! Added in 17/9/2018.")
    embed.add_field(name="Minor Update!", value="Some commands have cooldowns to prevent spam! Added in 8/31/2019.")
    embed.add_field(name="New Command!", value="Do !!diary to see other people's hidden messages in their diaries! Added in 18/8/2018.")
    embed.add_field(name="Updated Command!", value="Updated the !!love command. Now you can see how long people had loved together.")
    embed.add_field(name="Updated Command!", value="Updated the !!kill command. **You** can kill other people now!.")
    embed.add_field(name="Updated Command!", value="Updated the !!waud command. It should be more understandable now.")
    embed.add_field(name="New Command!", value="Do !!power to see your secret power! Added in 25/6/2018.")
    embed.add_field(name="New Command!", value="Do !!waud to see what other memebrs are doing. Added in 26/2/2018.")
    embed.add_field(name="Minor Update!", value="Every embed should have colours now! Updated in 13/1/2018.")
    embed.add_field(name="Updated Command!", value="Updated the !!help command. This time, it's an embed! Updated in 13/1/2018.")
    await client.say(embed=embed)
    
@client.command(pass_context=True)
async def reac(ctx):
    """A test command"""

    embed = discord.Embed(title="Going to be edited.", description="Thumbs up to update.")
    msgtest = await client.say(embed=embed)
    res = await client.wait_for_reaction(['👍', '👎'], message=msgtest)
    embed2 = discord.Embed(title="Embed1", description ="embed2")
    await client.edit_message(msgtest, embed=embed2)
        
@client.command(pass_context=True)
async def cd(ctx):
    """A test command"""

    await asyncio.sleep(10)
    await client.say("Wait for 10 seconds.")
                    
@client.command(pass_context = True)
async def mute(ctx, member: discord.Member):
    """Mutes a person on the server"""

    if ctx.message.author.server_permissions.administrator or ctx.message.author.id == '194151340090327041':
        role = discord.utils.get(member.server.roles, name='Muted')
        await client.add_roles(member, role)
        embed=discord.Embed(title="User Muted!", description="**{0}** was muted by **{1}**!".format(member, ctx.message.author), color=0xff00f6)
        await client.say(embed=embed)
    else:
        embed=discord.Embed(title="Permission Denied.", description="You don't have permission to use this command.", color=0xff00f6)
        await client.say(embed=embed)
    
@client.command(pass_context=True)
async def help(ctx):
    """List of all the commands!"""

    embed = discord.Embed(title="Diamond4Bot", description="A fun bot made by Diamond4luck#4795.")
    embed.add_field(name="Help Page", value="Click the number reactions below to look at different types of commands!")
    embed.add_field(name="Bot Related Commands", value="Mess around with the bot.")
    
    for i in client.commands():
        embed.add_field(name=i.name, value=i.help)
       
    await client.say(embed=embed)

@client.command(pass_context=True)
async def casino(ctx):
    """Win big!"""

    casinostart = await client.say("Bigger or smaller than 50? Say it!")

    def check(m):
        return 'Bigger', 'Smaller'
    
    message = await client.wait_for_message()
    if 'Bigger' in message.content:
        await client.say("Bigger? OK! Rolling!")
    elif 'Smaller' in message.content:
        await client.say("Smaller? OK! Rolling!")
    casinonumber = random.randint(0,100)
    sentcasinon = await client.say("{0}".format(casinonumber))
    casinonumber2 = random.randint(0,100)
    sentcasinon2 = await client.edit_message(sentcasinon,"{0}".format(casinonumber2))
    casinonumber3 = random.randint(0,100)
    sentcasinon3 = await client.edit_message(sentcasinon2,"{0}".format(casinonumber3))
    casinonumber4 = random.randint(0,100)
    sentcasinon4 = await client.edit_message(sentcasinon3,"{0}".format(casinonumber4))
    casinonumber5 = random.randint(0,100)    
    if casinonumber5 >= 50:
        await client.edit_message(sentcasinon4,"The number is {0}, which is bigger than 50!".format(casinonumber5))
    else:
        await client.edit_message(sentcasinon4,"The number is {0}, which is smaller than 50!".format(casinonumber5))
    if casinonumber5 >= 50:
        if 'Bigger' in message.content:
            await client.say("It was bigger than 50. You won!")
        else:
            await client.say("It was bigger than 50. You lost.")
    elif casinonumber5 <= 50:
        if 'Smaller' in message.content:
            await client.say("It was smaller than 50. You won!")
        else:
            await client.say("It was smaller than 50. You lost.")

@client.command(pass_context=True)
async def rps(ctx):
    """Rock, Scissor Paper!"""

    await client.say("Say Rock, Paper or Scissors!")
    
    def check(m):
        return 'Rock','Paper','Scissor'
    
    message = await client.wait_for_message()
    if 'Rock' in message.content:
        await client.say("You chose rock!")
    elif 'Paper' in message.content:
        await client.say("You chose paper!")
    elif 'Scissors' in message.content:
        await client.say("You chose scissors!")
    else:
        await client.say("Um, did you do something wrong?")
        
    rps1 = random.choice(["Rock","Paper","Scissors"])
    rpsdecision = await client.say(rps1)
    rps2 = random.choice(["Rock","Paper","Scissors"])
    rpsdecision2 = await client.edit_message(rpsdecision,"{}".format(rps2))
    rps3 = random.choice(["Rock","Paper","Scissors"])
    rpsdecision3 = await client.edit_message(rpsdecision2,"{}".format(rps3))
    rps4 = random.choice(["Rock","Paper","Scissors"])
    rpsdecision4 = await client.edit_message(rpsdecision3,"{}".format(rps4))
    rps5 = random.choice(["Rock","Paper","Scissors"])
    rpsdecision5 = await client.edit_message(rpsdecision4,"{}".format(rps5))

    if 'Rock' in rps5:
        if 'Rock' in message.content:
            await client.say("Rock versus Rock, it's a **tie!**")
        elif 'Paper' in message.content:
            await client.say("Paper versus Rock, Rock **wins!** You won!")
        elif 'Scissors' in message.content:
            await client.say("Scissors versus Rock, Rock **wins!** You lost!")
    elif 'Paper' in rps5:
        if 'Rock' in message.content:
            await client.say("Rock versus Paper, Paper **wins!** You lost!")
        elif 'Paper' in message.content:
            await client.say("Paper versus Paper, it's a **tie!**")
        elif 'Scissors' in message.content:
            await client.say("Scissors versus Paper, Scissors **wins!** You won!")
    elif 'Scissors' in rps5:
        if 'Rock' in message.content:
            await client.say("Rock versus Scissors, Rock **wins!** You won!")
        elif 'Paper' in message.content:
            await client.say("Paper versus Scissors, Paper **wins!** You lost!")
        elif 'Scissors' in message.content:
            await client.say("Scissors versus Scissors, it's a **tie!**")

@client.command(pass_context=True)
async def edit(ctx):
    """A test command"""

    edit = await client.say("Edit.")
    await client.add_reaction(edit,'2\u20e3')
    edit2 = await client.wait_for_reaction(['3\u20e3'], message=edit)
    await client.edit_message(edit, "Edited!")
    
@client.group(pass_context=True, invoke_without_command=True)
async def yon(ctx):
    """Yes or No?..."""
    yesornolist = open('./TextFiles/yesorno.txt').read().splitlines()
    yesornolist2 = random.choice(yesornolist)
    yon = await client.say(" {} Choose Y or N .".format(yesornolist2))
    await client.add_reaction(yon,'\U0001f1fe')
    await client.add_reaction(yon,'\U0001f1f3')
    
@yon.command(pass_context=True)
async def add(ctx,*, string):
    """Add's a Yes or No question"""

    yonopen = open("./TextFiles/yesorno.txt", "a")
    yonopen.write("\n{}".format(string))
    yonopen.close()
    await client.say("Added!")
    
    
@client.group(pass_context=True, invoke_without_command=True)
async def wyr(ctx):
    """Would you rather?..."""
    wyrlist = open('./TextFiles/wyr.txt').read().splitlines()
    wyrlist2 = random.choice(wyrlist)
    wyr = await client.say("Would you rather {}? Choose A or B.".format(wyrlist2))
    await client.add_reaction(wyr,'\U0001f170')
    await client.add_reaction(wyr,'\U0001f171')
    
@wyr.command(pass_context=True)
async def add(ctx,*, string):
    """Add's a would your rather question"""
    wyropen = open("./TextFiles/wyr.txt", "a")
    wyropen.write("\n{}".format(string))
    wyropen.close()
    await client.say("Added!")

@client.command(pass_context=True)
@commands.cooldown(1, 10, commands.BucketType.user)
async def kill(ctx):
    """Kills a user in the server"""

    kill = open('./TextFiles/Deaths.txt').read().splitlines()
    death = random.choice(kill)
    victim = random.choice([x for x in ctx.message.server.members if not x.bot])
    if ctx.message.author.id == "206027308149112832":
        embed = discord.Embed(title='A crime has been commited!', description = '<@!206027308149112832> killed {} {}!'.format(victim.display_name, death))
    else:
        embed = discord.Embed(title='A crime has been commited!', description = '{} killed {} {}!'.format(ctx.message.author.mention, victim.display_name, death))
    await client.say(embed=embed)
    
    
@client.command(pass_context=True)
async def kick(ctx, user: discord.Member):
    """Kicks a user from the server"""

    await client.say("Here's the boot. :boot: Bye bye, {}!".format(user.name))
    await client.kick(user)

@client.command(pass_context=True)
@commands.cooldown(1, 5, commands.BucketType.user)
async def game(ctx):
    """Shows a list of games you like to play."""

    game = open('./TextFiles/Games.txt').read().splitlines()
    games = random.choice(game)
    if ctx.message.author.id == "206027308149112832":
        await client.say("<@!206027308149112832> you like to play Clash Royale!")
    else:
        await client.say('%s you like to play %s' % (ctx.message.author.mention, games))

@client.command(pass_context=True)
async def test(ctx):
    """A test command"""
    await client.say('hi')
    greet = await client.wait_for_message(content='hi')
    await client.say('oo someone replied')
    greet2 = await client.wait_for_message(content='kill')
    await client.say('oi wanna fight')
    greet3 = await client.wait_for_message(content='ok m8 lets go')
    await client.say('ok lets dance u fat boi')
    await client.say('what are u gonna start off with')
 
    def fight(msg):
        return msg.content.startswith('Punch') or msg.content.startswith('Kick')
        
    message = await client.wait_for_message(check=fight)
    await client.say("your text here")
    
@client.command(pass_context = True)
async def listban(ctx):
    """Gets A List Of Users Who Are No Longer With us"""
    x = await client.get_bans(ctx.message.server)
    x = '\n'.join([y.name for y in x])
    embed = discord.Embed(title = "List of The Banned Idiots", description = x, color = 0xFFFFF)
    return await client.say(embed = embed) 

@client.command(pass_context=True, aliases=['remove', 'delete'])
async def purge(ctx, number):
    """Bulk-deletes messages from the channel."""
    try:
        if ctx.message.author.server_permissions.administrator:
            mgs = []  # Empty list to put all the messages in the log
            # Converting the amount of messages to delete to an integer
            number = int(number)
            async for x in client.logs_from(ctx.message.channel, limit=number):
                mgs.append(x)
            await client.delete_messages(mgs)
            print("Purged {} messages.".format(number))
            logger.info("Purged {} messages.".format(number))
        else:
            await client.say(config.err_mesg_permission)
    except:
        await client.say(config.err_mesg)
        
@client.command(pass_context=True)
async def roles(ctx):
    """Lists the current roles on the server."""
    
    result = "**The roles on this server are: {}**".format(', '.join([m.name for m in ctx.message.server.roles]))
    await client.say(result)

@client.command(pass_context=True)                    
async def moti(ctx):
    """Motivates you to do better!"""
    motivation = open('./TextFiles/moti2.txt', encoding = "UTF-8").read().splitlines()
    motivation2 = random.choice(motivation)
    embed = discord.Embed(title='Motivational Message for You!', description = '{}'.format(motivation2))
    embed.set_image(url="https://cdn.discordapp.com/attachments/385416830229151746/462809050053345322/images.jpg")
    await client.say(embed=embed)
    
@client.command(pass_context=True)
@commands.cooldown(1, 5, commands.BucketType.user)
async def love(ctx):
    """Finds a secret couple on the server."""

    love = random.choice([x for x in ctx.message.server.members if not x.bot])
    love2 = random.choice([x for x in ctx.message.server.members if not x.bot])  
    years = random.randint(0, 20)
    months = random.randint(0, 12)
    days = random.randint(0,32)
    embed = discord.Embed(title='We have found a secret couple in the server!', description = '{} loved {} for {} years, {} months and {} days!'.format(love.display_name, love2.display_name, years, months, days))
    embed.set_image(url="https://cdn.discordapp.com/attachments/385419071727992834/472017700110073876/download.jpg")
    await client.say(embed=embed)
    
                      

@client.command(pass_context=True, hidden=True)
async def embed(ctx):
    """A test command"""

    embed = discord.Embed(title='EMBED PLZ WORK', description='PLEASE MAKE THIS WORK')
    embed.set_image(url="https://cdn.discordapp.com/attachments/385419071727992834/393317821381345280/Wrong.png")
    await client.say(embed=embed)

@client.command(pass_context=True)
async def waud(ctx):
    """Predicts what you are doing!"""

    waud = open('./TextFiles/WAUD.txt').read().splitlines()
    wauds = random.choice(waud)
    wauddo = random.choice(["you are doing it right now!","you are not doing it right now, but later.","you are not doing it right now.","you don't do it at all."])
    waudhum = random.choice([x for x in ctx.message.server.members if not x.bot])
    await client.say(' {}, you are {}. If I had to guess, {}.'.format(waudhum.display_name,wauds,wauddo))
    
@client.command(pass_context=True)
async def ping(ctx):
    """Checks to see if the bot is working"""

    await client.say("Pong!")

@client.command(pass_context=True)
async def flip(ctx):
    """A good ol' flip of the coin"""

    flip = random.choice(["Heads","Tails","DA MIDDLE"])
    await client.say(flip)

@client.command(pass_context=True)
async def amIgay(ctx):
    """Decides if you are gay or not. P.S Results not 100% accurate"""

    Areyougay = random.choice(["Maybe","YES,DUH","NOPE"])
    await client.say(Areyougay)
    
@client.command(pass_context=True)
async def howIkms(ctx):
    """How you will die. P.S results no 100% accurate"""

    kms = random.choice (
        ["Jumping off from Trump's wall",
         "Eating too much KFC","Assassinated by Kim Jong Un",
         "Be surrounded by gay people","Killed by a goddamn clown",
         "Having Ebola, Cancer and Depression at the same time",
         "Be surrounded by creepers","Meeting Herobrine for the first time",
         "Attempting to kill hackers","Being as old as 9999 years old",
         "People calling you cringy/idiot"])
    
    await client.say(kms)

@client.command(pass_context=True)
async def pong(ctx):
    """Says Ping!"""

    await client.say("Ping!")

@client.command(pass_context=True)
async def pingpong(ctx):
    """Play ping-pong!"""

    await client.say("Pong Ping!")

@client.command(pass_context=True)
async def pongping(ctx):
    """Says Ping Pong Pung!"""

    await client.say("Ping Pong Pung!")

@client.command(pass_context=True)
async def pung(ctx):
    """Says pung"""

    await client.say("What do you expect me to say, huh? PINGPONGPUNGPUN?! WHAT THE HELL BRUH")

@client.command(pass_context=True)
async def roulette(ctx,*, string):
    """Picks a random user!"""

    roulette = random.choice([x for x in ctx.message.server.members if not x.bot])
    await client.say("The winner of ``%s`` is ``%s``" % (string, roulette.display_name))
    
@client.command(pass_context=True)
async def chance(ctx):
    """The chance of something happening."""
    luck = random.choice(
        ["Try again later",
         "Maybe","NOPE",
         "50% chance",
         "Definitely not",
         "Yes, definitely",
         "It depends on your fate",
         "Dunno, maybe ask the owner of this bot?"])
    
    await client.say(luck)

@client.command(pass_context=True)
async def future(ctx):
    """Shows you your future"""

    future = random.choice (["In the future, you may die early.",
                             "In the future, you may find a cute girl but didn't have a stable family.",
                             "In the future, you may found a rich girl, but she kept arguing with you. A few days later, you divorced her, and got depression until you got another relationship.",
                             "In the future, you found a braniac girl, but she is loyal to you and you got married happily. You got a good family and died in the age of 100.",
                             "In the future, you got your dream job, got a good wife, and got 2 good kids. You died in the age of 120.",
                             "In the future, you got your dream job, but your boss wants to fire you asap, so after working for a year, you got fired for no reason.",
                             "In the future, you didn't got your dream job, but the salary is high and your co-workers and your boss treats you like a family. You found love there too, and died in the age of 90 with happiness.",
                             "In the future,you won the lottery, and you earned 1$.","In the future, you won the lottery of 1 million dollars.",
                             "In the future, you bought a ticket for the lottery, but unluckily you lost.","In the future, you were forced to be in war. You died in the battlefield, but hey at least your name will be famous...",
                             "In the future, you died pretty early because you fell from a mountain.",
                             "`In the future, you met some famous youtubers, and they chose you as their sidekick.",
                             "In the future, you got what normal people do. A normal job, a normal family and a normal life. You died because of being too normal.",
                             "In the future, you became a millionaire and because of that, you donated a heck ton of money to the needy. In fact, you donated A LOT until you became famous and loved by everyone."])                               
    await client.say(future)
    
@client.command(pass_context=True)
async def number(ctx):
    """Picks a lucky number!"""

    luck = random.randint(0, 100)
    await client.say('Your lucky number for today is ``{0}``! Go use that number and win good stuff!'.format(luck))

@client.command(pass_context=True)
async def badnumber(ctx):
    """Picks a unlucky number!"""

    badnumber = random.randint(0,100)
    await client.say('Your unlucky number for today is ``{0}``! Try not to use this number or you will face the consequences...'.format(badnumber))

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
async def ban(ctx, member: discord.Member = None, *, reason = None):
    await member.ban(reason = reason)
    await ctx.send(f'**{member.display_name}** has been banned *{reason}*')

    if not member:
        await ctx.send('Please identify the person that you would like to ban. ')
        return
    
client.run(str(os.environ.get('BOT_TOKEN')))



