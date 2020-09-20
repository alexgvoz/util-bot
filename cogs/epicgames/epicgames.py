import requests

from cogs.epicgames import response

def get_promos():
    r = requests.get(
        "https://store-site-backend-static.ak.epicgames.com/freeGamesPromotions?locale=en-US&country=US&allowCountries=US")
    body = r.json()
    resp = response.EpicResponse.from_dict(body)
    promos = resp.data.catalog.search_store.elements
    return promos


def get_image_urls(promos):
    image_urls = []

    for promo in promos:
        for image in promo["keyImages"]:
            if image["type"] == "Thumbnail":
                image_urls.append(image["url"])

    return image_urls