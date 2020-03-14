import discord
from discord.ext import commands

class updates(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Events
    @commands.Cog.listener()
    async def on_ready(self):
        print('ready')

    @commands.Cog.listener()
    async def user_join(self, member : discord.Member):
        print(f'{member} has joined')
    
    @commands.Cog.listener()
    async def user_leave(self, member : discord.Member):
        print(f'{member} has left')
        

def setup(client):
    client.add_cog(updates(client))