import discord

from datetime import datetime
from discord.ext import commands
from cogs.epicgames import epicgames

client = commands.Bot(command_prefix="!")


# When bot boots up
@client.event
async def on_ready(guild_name=""):
    print("Bot is online.")
    for guild in client.guilds:
        if guild.name == guild_name:
            channel = client.get_channel("")

            promos = epicgames.get_promos()

            for i, promo in enumerate(promos):
                date = promo.effective_date.strftime("%m/%d/%y")
                today = datetime.now().strftime("%m/%d/%y")

                if date > today:
                    continue

                og_price = str(promo.price.total_price.original_price)
                price = f"${og_price[:-2]}.{og_price[-2:]}"
                end_date = promo.promotions.promotional_offers[0].promotional_offers[0].end_date.strftime("%m/%d/%y")
                dev = ""
                thumbnail = ""

                for image in promo.key_images:
                    if image.type == "Thumbnail":
                        thumbnail = image.url

                for atr in promo.custom_attributes:
                    if atr.key == "developerName":
                        dev = atr.value

                embed = discord.Embed(title=f"{promo.title}",
                                      description=f"| Promo Dates: {date} - {end_date}\n| Developer: {dev}\n| Original Price: {price}",
                                      color=discord.Color.blue(),
                                      url=f"https://www.epicgames.com/store/product/{promo.product_slug}")
                embed.set_image(url=thumbnail)

                await channel.send(embed=embed)