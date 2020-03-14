import discord
from discord.ext import commands

class admin(commands.Cog):

    def __init__(self, client):
        self.client = client

        # Commands
        @client.command()
        async def kick(self, ctx, member : discord.Member, *, reason=None):
            await member.kick(reason=reason)
            print(f'{member} has been kicked, reason: {reason}')

        @client.command()
        async def ban(self, ctx, member : discord.Member, *, reason=None):
            await member.ban(reason=reason)
            print(f'{member} has been banned, reason: {reason}')

        @client.command()
        async def clear(self, ctx, amount=None):
            if amount == None:
                await ctx.send('please specify an amount')
            else if amount != None:
                await ctx.purge(limit=amount)
                await ctx.send(f'{amount} messages purged')
                print(f'{amount} messages purged')

def setup(client):
    client.add_cog(admin(client))