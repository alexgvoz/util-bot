from discord.ext import commands
from cogs.epicgames import epicgames
from cogs import weather

client = commands.Bot(command_prefix="!")


# When bot boots up
@client.event
async def on_ready():
    print("Bot is online.")

    client.add_cog(epicgames.EpicPromos(client))
    client.add_cog(weather.Weather(client))

# TODO:
# Make free game url open Epic launcher
