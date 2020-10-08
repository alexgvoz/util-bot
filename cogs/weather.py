import os
import requests
import re
import sys

from dotenv import load_dotenv
from discord.ext import commands

# Get environment variable file
load_dotenv()
WEATHER_KEY = os.getenv("WEATHER_KEY")


# Validate postal code
def postal_validate(zip):
    zip_re = re.compile("^[0-9]{5}(?:-[0-9]{4})?$")

    m = zip_re.match(zip)

    if m:
        return True
    else:
        return False


# Get body from weather api
def get_weather_data(zip):
    if postal_validate(zip):
        r = requests.get(f"https://api.openweathermap.org/data/2.5/weather?zip={zip},us&appid=" + WEATHER_KEY)
        body = r.json()

        return body
    else:
        raise Exception("invalid zip code")


# Kelvin to Celsius
def to_celsius(t):
    return round(t - 273.15)


# Kelvin to Fahrenheit
def to_fahrenheit(t):
    return round((t - 273.15) * 9 / 5 + 32.0)

# Weather command used in Discord
class Weather(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Command that gets the weather for your zip code
    @commands.command(pass_context=True, help="Gets the weather for your zip code. (zip code, temperature scale)")
    async def weather(self, ctx, zip, temp_type="f"):
        data = None

        try:
            data = get_weather_data(zip)
        except Exception:
            _, value, _ = sys.exc_info()
            await ctx.send("Error: " + str(value))

        text = f"""The weather in {data["name"]} is currently {to_fahrenheit(data["main"]["temp"])} degrees Fahrenheit"""

        if temp_type.lower() == "c":
            text = f"""The weather in {data["name"]} is currently {to_celsius(data["main"]["temp"])} degrees Celsius"""

        await ctx.send(text)
