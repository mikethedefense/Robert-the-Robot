import discord
import time
import random
import asyncio
from datetime import datetime,timedelta
from discord.ext import commands
import random

client = commands.Bot(command_prefix="!")
client.remove_command("help")
# Variables
lis = ["Gay","Lesbian"]
start_time = time.time()
buddy = int(371652098468872192)

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name= "cards with wise guys"))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.lower() == "hello":
        await message.channel.send("Hello there mister <@%d>" % message.author.id)
    await client.process_commands(message)

@client.command()
async def hello(ctx):
    await ctx.send("Hello!")

@client.command()
async def ping(ctx, arg1: discord.Member):
    print("Here's his information! %s %d " % (str(arg1.name),int(arg1.id)))
    await ctx.send("Hey %s, how are you doing? <@%d>" % (str(arg1.name),int(arg1.id)))

@client.command(name="server")
async def pri(ctx):
    await ctx.send("Here's some info! Server member count: %d, your name: %s, your ID: %d, this channel: %s" % (ctx.guild.member_count,ctx.author.name,ctx.author.id,ctx.channel.name))

@client.command()
async def hgl(ctx,arg2: discord.Member):
    rand = random.choice(lis)
    rad = random.randint(0,100)
    await ctx.send("{} is {} % {}".format(str(arg2.name),rad,rand))

@client.command()
async def info(ctx,arg: discord.Member):
    em = discord.Embed(title = "Information on {}".format(str(arg.name)), colour = 0x343deb)
    em.add_field(name="Name",value="{}".format(arg.name), inline=False)
    em.add_field(name="ID", value = "{}".format(arg.id, inline = False))
    em.add_field(name="Joined Server at", value= "{}".format((arg.joined_at)), inline=False)
    for activity in arg.activities: 
        em.add_field(name="Activity", value= "{}".format(activity.name.title()),inline=False)
    if arg.activities == ():
        em.add_field(name = "Activity", value = "No Activities to Show here!", inline = False)
    em.add_field(name="Roles", value = "{}".format(arg.top_role),inline = False)
    em.add_field(name = "Status", value = "{}".format(str(arg.status).title()),inline = False)
    await ctx.send(embed = em)
@client.command()
async def time(ctx):
    await ctx.send(datetime.now.strftime("%H:%M:%S"))

@client.command()
async def help(ctx):
    author = ctx.message.author
    embed = discord.Embed(title = "Help", colour = discord.Colour.red())
    embed.add_field(name="hello", value="Returns: Hello there mister @(user)",inline = False)
    embed.add_field(name = "!hello", value = "Returns: Hello!", inline = False)
    embed.add_field(name="!ping (user)", value = "Returns user's information and pings the user", inline = False)
    embed.add_field(name = "!hgl (user)", value = "Returns how gay/lesbian the user you put is",inline = False)
    embed.add_field(name = "!info (user)", value = "Returns detailed user information", inline = True)
    embed.add_field(name = "!time", value = "Returns current time", inline = False)
    embed.add_field(name = "!uptime", value = "Returns bot's uptime", inline = False)
    embed.add_field(name = "!server", value = "Returns server info", inline = False)
    await ctx.send(embed = embed)

@client.command()
async def uptime(ctx):
    current_time = time.time()
    difference_seconds = int(current_time - start_time)
    difference = timedelta(seconds=difference_seconds)
    e = discord.Embed(title = "My uptime", colour = discord.Colour.dark_gold())
    e.set_footer(text = difference)
    await ctx.send(embed = e)

client.run("token")
