import discord
from discord import message
from discord.embeds import Embed
from discord.ext import commands
import random
import requests
print("Starting bot...")
client=discord.Client()
client = commands.Bot(command_prefix = '.')
@client.command(
	brief="Print bot reply speed."
)
async def ping(ctx):
    await ctx.channel.send(f'Pong! {round (client.latency * 1000)}ms ')
@client.command(
    brief="Print as it is!"
)
async def copy_words(ctx,*args):
    manywords = ""
    for arg in args:
        manywords = manywords + " " + arg
    await ctx.channel.send(manywords)
@client.command(
    brief="a pic that represent emotion:"
)
async def emoji(ctx):
    await ctx.channel.send(":rolling_eyes:")
@client.command()
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')
@client.command()
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!!!!!'
    )
client.run("token")
