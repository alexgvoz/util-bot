import sys
from bot import client
from integrations import weather

# Command that gets the weather for your zip code
@client.command(name="weather", help="Gets the weather for your zip code. (zip code, temperature scale)")
async def get_weather(ctx, zip, temp_type = "f"):
    data = None

    try:
        data = weather.get_weather_data(zip)
    except Exception:
        _, value, _ = sys.exc_info()
        await ctx.send('Error: ' + value)

    text = f"""The weather in {data["name"]} is currently {weather.to_fahrenheit(data["main"]["temp"])} degrees Fahrenheit"""

    if temp_type.lower() == "c":
        text = f"""The weather in {data["name"]} is currently {weather.to_celsius(data["main"]["temp"])} degrees Celsius"""

    await ctx.send(text)