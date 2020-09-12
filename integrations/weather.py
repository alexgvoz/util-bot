import os
import json
import requests
import re
from dotenv import load_dotenv

# Get environment variable file
load_dotenv()
WEATHER_KEY= os.getenv('WEATHER_KEY')

# Validate postal code
def postal_validate(zip):
    zip_re = re.compile("^[0-9]{5}(?:-[0-9]{4})?$")

    m = zip_re.match(zip)

    if m:
        return True
    elif m is None:
        return False

# Contact weather api and return body
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