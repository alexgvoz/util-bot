import discord
from discord.ext import commands

client = commands.Bot(command_prefix="!")

# When bot boots up
@client.event
async def on_ready():
    print("Bot is online.")