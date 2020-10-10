import requests
import discord

from discord.ext import commands, tasks
from datetime import datetime
from cogs.epicgames import response


# Grabs promos from Epic Store
def get_promos():
    r = requests.get(
        "https://store-site-backend-static.ak.epicgames.com/freeGamesPromotions?locale=en-US&country=US&allowCountries=US")
    body = r.json()
    resp = response.EpicResponse.from_dict(body)
    promos = resp.data.catalog.search_store.elements
    return promos


def hours_until_thursday():
    pass


class EpicPromos(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.post_promos.start()

        for guild in client.guilds:
            if guild.name == "Nerds":
                self.channel = guild.get_channel(755242779076067358)

    @tasks.loop(hours=1)
    async def post_promos(self):
        promos = get_promos()

        for promo in promos:
            date = promo.effective_date.strftime("%m/%d/%y")
            today = datetime.now().strftime("%m/%d/%y")

            if date > today:
                continue

            og_price = str(promo.price.total_price.original_price)
            price = f"${og_price[:-2]}.{og_price[-2:]}"
            try:
                end_date = promo.promotions.promotional_offers[0].promotional_offers[0].end_date.strftime("%m/%d/%y")
            except:
                continue
            dev = ""
            thumbnail = ""

            for image in promo.key_images:
                if image.type == "Thumbnail":
                    thumbnail = image.url

            for atr in promo.custom_attributes:
                if atr.key == "developerName":
                    dev = atr.value

            embed = discord.Embed(title=f"{promo.title}",
                                  description=f"| Promo Dates: {date} - {end_date}\n"
                                              f"| Developer: {dev}\n"
                                              f"| Original Price: {price}",
                                  color=discord.Color.blue(),
                                  url=f"https://www.epicgames.com/store/product/{promo.product_slug}")
            embed.set_image(url=thumbnail)

            await self.channel.send(embed=embed)

    def cog_unload(self):
        self.post_promos.cancel()
