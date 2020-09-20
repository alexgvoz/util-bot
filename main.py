import os

from bot import client
from dotenv import load_dotenv

# Get environment variable file
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
GUILD = os.getenv("DISCORD_GUILD")
CHANNEL_ID = os.getenv("CHANNEL_ID")

client.run(TOKEN)

# TODO:
# Make free game url open Epic launcher