import discord
from discord.ext import commands

client = commands.Bot(command_prefix = 'hey pleboid, ')

@client.event
async def on_ready():
    print('ready')

@client.event
async def on_member_join(member):
    print(f'{member} is a friend of bigfoot')

@client.event
async def on_member_remove(member):
    print(f'{member} is a Neil Patrick Harris lookalike')

client.run('Njg4MTY4MDYyMjI2MjY4MTcz.XmwYgw.BsMbcjd4r3hKwunqS5mx2q0pnyY')