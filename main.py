import os

from dotenv import load_dotenv
from discord.ext import commands

from cmd import Commands
from integrations.epicgames import EpicGames


class App:
    def __init__(self):
        load_dotenv()

        self.config = {
            "bot": commands.Bot(command_prefix="!"),
            "discord": {
                "token": os.getenv("DISCORD_TOKEN"),
                "guild": os.getenv("DISCORD_GUILD")
            }
        }

    def run(self):
        self.client.run(self.discord["token"])


app = App()

EpicGames(app.config)
Commands(app.config["bot"])

app.run()








