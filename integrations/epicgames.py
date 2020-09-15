from io import BytesIO
from aiohttp import ClientSession
from integrations import Integration


class EpicGames(Integration):
def x():
    async with ClientSession() as session:
        async with session.get(
                "https://cdn1.epicgames.com/27d2f156f77b4202b9bc78e40a408b03/offer/EGS_WhereTheWaterTastesLikeWine_DimBulbGames_S1-2560x1440-75b8bde822ddf61974fe34cc0fb6f26c.jpg") as resp:
            if resp.status != 200:
                return await channel.send('Could not download file...')
            data = BytesIO(await resp.read())
            await channel.send(file=discord.File(data, 'cool_image.png'))
