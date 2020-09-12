import os
import cmd
from bot import client
from dotenv import load_dotenv

# Get environment variable file
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
GUILD = os.getenv("DISCORD_GUILD")

client.run(TOKEN)