import discord
from discord.ext import commands

class fun(commands.Cog):

    def __init__(self, client):
        self.client = client

        # Commands
    @client.command()
    async def suck(self, ctx):
        await ctx.send(f':eggplant: :yum: {ctx.author}')

def setup(client):
    client.add_cog(fun(client))