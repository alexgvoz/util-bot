from io import BytesIO
from aiohttp import ClientSession

async def to_image(url):
    async with ClientSession() as session:
        async with session.get(url) as resp:
            if resp.status != 200:
                return None

            data = BytesIO(await resp.read())

            return data