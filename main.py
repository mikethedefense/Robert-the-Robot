import discord
import time
import random
import asyncio
import datetime
from discord.ext import commands
import logging



client = commands.Bot(command_prefix="!")


# Variables

buddy = int(371652098468872192)

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="cards with wise guys"))

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



@client.command(name="print")
async def pri(ctx):
    await ctx.send("Here's some info! Server member count: %d, your name: %s, your ID: %d, this channel: %s" % (ctx.guild.member_count,ctx.author.name,ctx.author.id,ctx.channel.name))

client.run("token")