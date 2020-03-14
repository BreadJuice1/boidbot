import discord
import os
from discord.ext import commands
import random

client = commands.Bot(command_prefix = 'hey pleboid, ')

@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    print(f'cogs.{extension} loaded')
    await ctx.send(f'cogs.{extension} loaded')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    print(f'cogs.{extension} unloaded')
    await ctx.send(f'cogs.{extension} unloaded')
      
@client.command()
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')
    print(f'cogs.{extension} reloaded')
    await ctx.send(f'cogs.{extension} reloaded')

    
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')
        print(f'cogs.{filename[:-3]} loaded')

client.run('Njg4MTY4MDYyMjI2MjY4MTcz.XmwYgw.BsMbcjd4r3hKwunqS5mx2q0pnyY')