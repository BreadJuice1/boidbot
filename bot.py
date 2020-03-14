import discord
from discord.ext import commands
import random

client = commands.Bot(command_prefix = 'hey pleboid, ')

@client.event
async def on_ready():
    print('ready')

@client.event
async def on_member_join(member):
    print(f'{member} has joined')

@client.event
async def on_member_remove(member):
    print(f'{member} has left')

@client.command()
async def bruh(ctx):
    await ctx.send(f'Bruh! {round(client.latency * 1000)}ms')

@client.command(aliases=['test'])
async def breh(ctx, *, question):
    responses = ['ple', 'boid', 'pleboid']
    await ctx.send(f'{question}\n{random.choice(responses)}')
    

client.run('Njg4MTY4MDYyMjI2MjY4MTcz.XmwYgw.BsMbcjd4r3hKwunqS5mx2q0pnyY')