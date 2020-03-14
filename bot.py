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

@client.command()
async def load_all(ctx):
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            client.load_extension(f'cogs.{filename[:-3]}')
            print(f'cogs.{filename[:-3]} loaded')
            await ctx.send(f'cogs.{filename[:-3]} loaded')

@client.command()
async def unload_all(ctx):
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            client.unload_extension(f'cogs.{filename[:-3]}')
            print(f'cogs.{filename[:-3]} unloaded')
            await ctx.send(f'cogs.{filename[:-3]} unloaded')

@client.command()
@commands.is_owner()
async def shutdown(ctx):
    await ctx.bot.logout()

client.run('Njg4MTY4MDYyMjI2MjY4MTcz.XmxLMQ.I1KQB2o1br2FmCZf0hWL80ymD-4')