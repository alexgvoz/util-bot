import os
import cmd
from bot import client
from dotenv import load_dotenv
from discord.ext import commands


class App:
    def __init__(self):
        load_dotenv()

        self.client = commands.Bot(command_prefix="!")
        self.discord = {
            "token": os.getenv("DISCORD_TOKEN"),
            "guild": os.getenv("DISCORD_GUILD")
        }
    
    def run(self):
        self.client.run(self.discord["token"])