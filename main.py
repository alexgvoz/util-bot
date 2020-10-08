import os

from dotenv import load_dotenv
from bot import client

# Get environment variable file
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
GUILD = os.getenv("DISCORD_GUILD")
CHANNEL_ID = os.getenv("CHANNEL_ID")

client.run(TOKEN)