# This code parses date/times, so please
#
#     pip install python-dateutil
#
# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = epic_response_from_dict(json.loads(json_string))
import dateutil.parser

from dataclasses import dataclass
from typing import Any, List, Union, TypeVar, Type, cast, Callable
from datetime import datetime


T = TypeVar("T")


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_datetime(x: Any) -> datetime:
    return dateutil.parser.parse(x)


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_none(x: Any) -> Any:
    assert x is None
    return x


def from_union(fs, x):
    for f in fs:
        try:
            return f(x)
        except:
            pass
    assert False


@dataclass
class Category:
    path: str

    @staticmethod
    def from_dict(obj: Any) -> 'Category':
        assert isinstance(obj, dict)
        path = from_str(obj.get("path"))
        return Category(path)

    def to_dict(self) -> dict:
        result: dict = {}
        result["path"] = from_str(self.path)
        return result


@dataclass
class CustomAttribute:
    key: str
    value: str

    @staticmethod
    def from_dict(obj: Any) -> 'CustomAttribute':
        assert isinstance(obj, dict)
        key = from_str(obj.get("key"))
        value = from_str(obj.get("value"))
        return CustomAttribute(key, value)

    def to_dict(self) -> dict:
        result: dict = {}
        result["key"] = from_str(self.key)
        result["value"] = from_str(self.value)
        return result


@dataclass
class Item:
    id: str
    namespace: str

    @staticmethod
    def from_dict(obj: Any) -> 'Item':
        assert isinstance(obj, dict)
        id = from_str(obj.get("id"))
        namespace = from_str(obj.get("namespace"))
        return Item(id, namespace)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_str(self.id)
        result["namespace"] = from_str(self.namespace)
        return result


@dataclass
class KeyImage:
    type: str
    url: str

    @staticmethod
    def from_dict(obj: Any) -> 'KeyImage':
        assert isinstance(obj, dict)
        type = from_str(obj.get("type"))
        url = from_str(obj.get("url"))
        return KeyImage(type, url)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_str(self.type)
        result["url"] = from_str(self.url)
        return result


@dataclass
class AppliedRuleDiscountSetting:
    discount_type: str

    @staticmethod
    def from_dict(obj: Any) -> 'AppliedRuleDiscountSetting':
        assert isinstance(obj, dict)
        discount_type = from_str(obj.get("discountType"))
        return AppliedRuleDiscountSetting(discount_type)

    def to_dict(self) -> dict:
        result: dict = {}
        result["discountType"] = from_str(self.discount_type)
        return result


@dataclass
class AppliedRule:
    id: str
    end_date: datetime
    discount_setting: AppliedRuleDiscountSetting

    @staticmethod
    def from_dict(obj: Any) -> 'AppliedRule':
        assert isinstance(obj, dict)
        id = from_str(obj.get("id"))
        end_date = from_datetime(obj.get("endDate"))
        discount_setting = AppliedRuleDiscountSetting.from_dict(obj.get("discountSetting"))
        return AppliedRule(id, end_date, discount_setting)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_str(self.id)
        result["endDate"] = self.end_date.isoformat()
        result["discountSetting"] = to_class(AppliedRuleDiscountSetting, self.discount_setting)
        return result


@dataclass
class LineOffer:
    applied_rules: List[AppliedRule]

    @staticmethod
    def from_dict(obj: Any) -> 'LineOffer':
        assert isinstance(obj, dict)
        applied_rules = from_list(AppliedRule.from_dict, obj.get("appliedRules"))
        return LineOffer(applied_rules)

    def to_dict(self) -> dict:
        result: dict = {}
        result["appliedRules"] = from_list(lambda x: to_class(AppliedRule, x), self.applied_rules)
        return result


@dataclass
class CurrencyInfo:
    decimals: int

    @staticmethod
    def from_dict(obj: Any) -> 'CurrencyInfo':
        assert isinstance(obj, dict)
        decimals = from_int(obj.get("decimals"))
        return CurrencyInfo(decimals)

    def to_dict(self) -> dict:
        result: dict = {}
        result["decimals"] = from_int(self.decimals)
        return result


@dataclass
class FmtPrice:
    original_price: str
    discount_price: str
    intermediate_price: str

    @staticmethod
    def from_dict(obj: Any) -> 'FmtPrice':
        assert isinstance(obj, dict)
        original_price = from_str(obj.get("originalPrice"))
        discount_price = from_str(obj.get("discountPrice"))
        intermediate_price = from_str(obj.get("intermediatePrice"))
        return FmtPrice(original_price, discount_price, intermediate_price)

    def to_dict(self) -> dict:
        result: dict = {}
        result["originalPrice"] = from_str(self.original_price)
        result["discountPrice"] = from_str(self.discount_price)
        result["intermediatePrice"] = from_str(self.intermediate_price)
        return result


@dataclass
class TotalPrice:
    discount_price: int
    original_price: int
    voucher_discount: int
    discount: int
    currency_code: str
    currency_info: CurrencyInfo
    fmt_price: FmtPrice

    @staticmethod
    def from_dict(obj: Any) -> 'TotalPrice':
        assert isinstance(obj, dict)
        discount_price = from_int(obj.get("discountPrice"))
        original_price = from_int(obj.get("originalPrice"))
        voucher_discount = from_int(obj.get("voucherDiscount"))
        discount = from_int(obj.get("discount"))
        currency_code = from_str(obj.get("currencyCode"))
        currency_info = CurrencyInfo.from_dict(obj.get("currencyInfo"))
        fmt_price = FmtPrice.from_dict(obj.get("fmtPrice"))
        return TotalPrice(discount_price, original_price, voucher_discount, discount, currency_code, currency_info, fmt_price)

    def to_dict(self) -> dict:
        result: dict = {}
        result["discountPrice"] = from_int(self.discount_price)
        result["originalPrice"] = from_int(self.original_price)
        result["voucherDiscount"] = from_int(self.voucher_discount)
        result["discount"] = from_int(self.discount)
        result["currencyCode"] = from_str(self.currency_code)
        result["currencyInfo"] = to_class(CurrencyInfo, self.currency_info)
        result["fmtPrice"] = to_class(FmtPrice, self.fmt_price)
        return result


@dataclass
class Price:
    total_price: TotalPrice
    line_offers: List[LineOffer]

    @staticmethod
    def from_dict(obj: Any) -> 'Price':
        assert isinstance(obj, dict)
        total_price = TotalPrice.from_dict(obj.get("totalPrice"))
        line_offers = from_list(LineOffer.from_dict, obj.get("lineOffers"))
        return Price(total_price, line_offers)

    def to_dict(self) -> dict:
        result: dict = {}
        result["totalPrice"] = to_class(TotalPrice, self.total_price)
        result["lineOffers"] = from_list(lambda x: to_class(LineOffer, x), self.line_offers)
        return result


@dataclass
class PromotionalOfferDiscountSetting:
    discount_type: str
    discount_percentage: int

    @staticmethod
    def from_dict(obj: Any) -> 'PromotionalOfferDiscountSetting':
        assert isinstance(obj, dict)
        discount_type = from_str(obj.get("discountType"))
        discount_percentage = from_int(obj.get("discountPercentage"))
        return PromotionalOfferDiscountSetting(discount_type, discount_percentage)

    def to_dict(self) -> dict:
        result: dict = {}
        result["discountType"] = from_str(self.discount_type)
        result["discountPercentage"] = from_int(self.discount_percentage)
        return result


@dataclass
class PromotionalOfferPromotionalOffer:
    start_date: datetime
    end_date: datetime
    discount_setting: PromotionalOfferDiscountSetting

    @staticmethod
    def from_dict(obj: Any) -> 'PromotionalOfferPromotionalOffer':
        assert isinstance(obj, dict)
        start_date = from_datetime(obj.get("startDate"))
        end_date = from_datetime(obj.get("endDate"))
        discount_setting = PromotionalOfferDiscountSetting.from_dict(obj.get("discountSetting"))
        return PromotionalOfferPromotionalOffer(start_date, end_date, discount_setting)

    def to_dict(self) -> dict:
        result: dict = {}
        result["startDate"] = self.start_date.isoformat()
        result["endDate"] = self.end_date.isoformat()
        result["discountSetting"] = to_class(PromotionalOfferDiscountSetting, self.discount_setting)
        return result


@dataclass
class PromotionalOffer:
    promotional_offers: List[PromotionalOfferPromotionalOffer]

    @staticmethod
    def from_dict(obj: Any) -> 'PromotionalOffer':
        assert isinstance(obj, dict)
        promotional_offers = from_list(PromotionalOfferPromotionalOffer.from_dict, obj.get("promotionalOffers"))
        return PromotionalOffer(promotional_offers)

    def to_dict(self) -> dict:
        result: dict = {}
        result["promotionalOffers"] = from_list(lambda x: to_class(PromotionalOfferPromotionalOffer, x), self.promotional_offers)
        return result


@dataclass
class Promotions:
    promotional_offers: List[PromotionalOffer]
    upcoming_promotional_offers: List[PromotionalOffer]

    @staticmethod
    def from_dict(obj: Any) -> 'Promotions':
        assert isinstance(obj, dict)
        promotional_offers = from_list(PromotionalOffer.from_dict, obj.get("promotionalOffers"))
        upcoming_promotional_offers = from_list(PromotionalOffer.from_dict, obj.get("upcomingPromotionalOffers"))
        return Promotions(promotional_offers, upcoming_promotional_offers)

    def to_dict(self) -> dict:
        result: dict = {}
        result["promotionalOffers"] = from_list(lambda x: to_class(PromotionalOffer, x), self.promotional_offers)
        result["upcomingPromotionalOffers"] = from_list(lambda x: to_class(PromotionalOffer, x), self.upcoming_promotional_offers)
        return result


@dataclass
class Seller:
    id: str
    name: str

    @staticmethod
    def from_dict(obj: Any) -> 'Seller':
        assert isinstance(obj, dict)
        id = from_str(obj.get("id"))
        name = from_str(obj.get("name"))
        return Seller(id, name)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_str(self.id)
        result["name"] = from_str(self.name)
        return result


@dataclass
class Tag:
    id: int

    @staticmethod
    def from_dict(obj: Any) -> 'Tag':
        assert isinstance(obj, dict)
        id = int(from_str(obj.get("id")))
        return Tag(id)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_str(str(self.id))
        return result


@dataclass
class Element:
    title: str
    id: str
    namespace: str
    description: str
    effective_date: datetime
    key_images: List[KeyImage]
    seller: Seller
    product_slug: str
    url_slug: str
    url: None
    items: List[Item]
    custom_attributes: List[CustomAttribute]
    categories: List[Category]
    tags: List[Tag]
    price: Price
    promotions: Promotions

    @staticmethod
    def from_dict(obj: Any) -> 'Element':
        assert isinstance(obj, dict)
        title = from_str(obj.get("title"))
        id = from_str(obj.get("id"))
        namespace = from_str(obj.get("namespace"))
        description = from_str(obj.get("description"))
        effective_date = from_datetime(obj.get("effectiveDate"))
        key_images = from_list(KeyImage.from_dict, obj.get("keyImages"))
        seller = Seller.from_dict(obj.get("seller"))
        product_slug = from_str(obj.get("productSlug"))
        url_slug = from_str(obj.get("urlSlug"))
        url = from_none(obj.get("url"))
        items = from_list(Item.from_dict, obj.get("items"))
        custom_attributes = from_list(CustomAttribute.from_dict, obj.get("customAttributes"))
        categories = from_list(Category.from_dict, obj.get("categories"))
        tags = from_list(Tag.from_dict, obj.get("tags"))
        price = Price.from_dict(obj.get("price"))
        promotions = Promotions.from_dict(obj.get("promotions"))
        return Element(title, id, namespace, description, effective_date, key_images, seller, product_slug, url_slug, url, items, custom_attributes, categories, tags, price, promotions)

    def to_dict(self) -> dict:
        result: dict = {}
        result["title"] = from_str(self.title)
        result["id"] = from_str(self.id)
        result["namespace"] = from_str(self.namespace)
        result["description"] = from_str(self.description)
        result["effectiveDate"] = self.effective_date.isoformat()
        result["keyImages"] = from_list(lambda x: to_class(KeyImage, x), self.key_images)
        result["seller"] = to_class(Seller, self.seller)
        result["productSlug"] = from_str(self.product_slug)
        result["urlSlug"] = from_str(self.url_slug)
        result["url"] = from_none(self.url)
        result["items"] = from_list(lambda x: to_class(Item, x), self.items)
        result["customAttributes"] = from_list(lambda x: to_class(CustomAttribute, x), self.custom_attributes)
        result["categories"] = from_list(lambda x: to_class(Category, x), self.categories)
        result["tags"] = from_list(lambda x: to_class(Tag, x), self.tags)
        result["price"] = to_class(Price, self.price)
        result["promotions"] = to_class(Promotions, self.promotions)
        return result


@dataclass
class Paging:
    count: int
    total: int

    @staticmethod
    def from_dict(obj: Any) -> 'Paging':
        assert isinstance(obj, dict)
        count = from_int(obj.get("count"))
        total = from_int(obj.get("total"))
        return Paging(count, total)

    def to_dict(self) -> dict:
        result: dict = {}
        result["count"] = from_int(self.count)
        result["total"] = from_int(self.total)
        return result


@dataclass
class SearchStore:
    elements: List[Element]
    paging: Paging

    @staticmethod
    def from_dict(obj: Any) -> 'SearchStore':
        assert isinstance(obj, dict)
        elements = from_list(Element.from_dict, obj.get("elements"))
        paging = Paging.from_dict(obj.get("paging"))
        return SearchStore(elements, paging)

    def to_dict(self) -> dict:
        result: dict = {}
        result["elements"] = from_list(lambda x: to_class(Element, x), self.elements)
        result["paging"] = to_class(Paging, self.paging)
        return result


@dataclass
class Catalog:
    search_store: SearchStore

    @staticmethod
    def from_dict(obj: Any) -> 'Catalog':
        assert isinstance(obj, dict)
        search_store = SearchStore.from_dict(obj.get("searchStore"))
        return Catalog(search_store)

    def to_dict(self) -> dict:
        result: dict = {}
        result["searchStore"] = to_class(SearchStore, self.search_store)
        return result


@dataclass
class Data:
    catalog: Catalog

    @staticmethod
    def from_dict(obj: Any) -> 'Data':
        assert isinstance(obj, dict)
        catalog = Catalog.from_dict(obj.get("Catalog"))
        return Data(catalog)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Catalog"] = to_class(Catalog, self.catalog)
        return result


@dataclass
class Hint:
    path: List[Union[int, str]]
    max_age: int

    @staticmethod
    def from_dict(obj: Any) -> 'Hint':
        assert isinstance(obj, dict)
        path = from_list(lambda x: from_union([from_int, from_str], x), obj.get("path"))
        max_age = from_int(obj.get("maxAge"))
        return Hint(path, max_age)

    def to_dict(self) -> dict:
        result: dict = {}
        result["path"] = from_list(lambda x: from_union([from_int, from_str], x), self.path)
        result["maxAge"] = from_int(self.max_age)
        return result


@dataclass
class CacheControl:
    version: int
    hints: List[Hint]

    @staticmethod
    def from_dict(obj: Any) -> 'CacheControl':
        assert isinstance(obj, dict)
        version = from_int(obj.get("version"))
        hints = from_list(Hint.from_dict, obj.get("hints"))
        return CacheControl(version, hints)

    def to_dict(self) -> dict:
        result: dict = {}
        result["version"] = from_int(self.version)
        result["hints"] = from_list(lambda x: to_class(Hint, x), self.hints)
        return result


@dataclass
class Extensions:
    cache_control: CacheControl

    @staticmethod
    def from_dict(obj: Any) -> 'Extensions':
        assert isinstance(obj, dict)
        cache_control = CacheControl.from_dict(obj.get("cacheControl"))
        return Extensions(cache_control)

    def to_dict(self) -> dict:
        result: dict = {}
        result["cacheControl"] = to_class(CacheControl, self.cache_control)
        return result


@dataclass
class EpicResponse:
    data: Data
    extensions: Extensions

    @staticmethod
    def from_dict(obj: Any) -> 'EpicResponse':
        assert isinstance(obj, dict)
        data = Data.from_dict(obj.get("data"))
        extensions = Extensions.from_dict(obj.get("extensions"))
        return EpicResponse(data, extensions)

    def to_dict(self) -> dict:
        result: dict = {}
        result["data"] = to_class(Data, self.data)
        result["extensions"] = to_class(Extensions, self.extensions)
        return result


def epic_response_from_dict(s: Any) -> EpicResponse:
    return EpicResponse.from_dict(s)


def epic_response_to_dict(x: EpicResponse) -> Any:
    return to_class(EpicResponse, x)
