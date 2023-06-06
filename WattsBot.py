import discord
import os

from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN=os.getenv('DISCORD_TOKEN')


intents = discord.Intents.all()

client = commands.Bot(command_prefix='!', intents=intents)

@client.command()
async def hello(ctx):
    await ctx.send("Hey there!")


@client.command()
async def clearchannel(ctx):
    await ctx.channel.purge()


client.run(TOKEN)