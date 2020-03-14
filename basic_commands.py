import discord
from discord.ext import commands

class basic_commands(commands.Cog):

    def __init__(self, client):
        self.client = client