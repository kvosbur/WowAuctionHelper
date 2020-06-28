# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = get_auction_from_dict(json.loads(json_string))

from dataclasses import dataclass
from typing import Any, Optional, List, TypeVar, Callable, Type, cast
from enum import Enum
from Models.helpers import *


@dataclass
class Item:
    id: int
    context: Optional[int] = None
    bonus_lists: Optional[List[int]] = None
    modifiers: Optional[List[Modifier]] = None
    pet_breed_id: Optional[int] = None
    pet_level: Optional[int] = None
    pet_quality_id: Optional[int] = None
    pet_species_id: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Item':
        assert isinstance(obj, dict)
        id = from_int(obj.get("id"))
        context = from_union([from_int, from_none], obj.get("context"))
        bonus_lists = from_union([lambda x: from_list(from_int, x), from_none], obj.get("bonus_lists"))
        modifiers = from_union([lambda x: from_list(Modifier.from_dict, x), from_none], obj.get("modifiers"))
        pet_breed_id = from_union([from_int, from_none], obj.get("pet_breed_id"))
        pet_level = from_union([from_int, from_none], obj.get("pet_level"))
        pet_quality_id = from_union([from_int, from_none], obj.get("pet_quality_id"))
        pet_species_id = from_union([from_int, from_none], obj.get("pet_species_id"))
        return Item(id, context, bonus_lists, modifiers, pet_breed_id, pet_level, pet_quality_id, pet_species_id)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_int(self.id)
        result["context"] = from_union([from_int, from_none], self.context)
        result["bonus_lists"] = from_union([lambda x: from_list(from_int, x), from_none], self.bonus_lists)
        result["modifiers"] = from_union([lambda x: from_list(lambda x: to_class(Modifier, x), x), from_none], self.modifiers)
        result["pet_breed_id"] = from_union([from_int, from_none], self.pet_breed_id)
        result["pet_level"] = from_union([from_int, from_none], self.pet_level)
        result["pet_quality_id"] = from_union([from_int, from_none], self.pet_quality_id)
        result["pet_species_id"] = from_union([from_int, from_none], self.pet_species_id)
        return result


class TimeLeft(Enum):
    LONG = "LONG"
    MEDIUM = "MEDIUM"
    SHORT = "SHORT"
    VERY_LONG = "VERY_LONG"


@dataclass
class Auction:
    id: int
    item: Item
    quantity: int
    time_left: TimeLeft
    buyout: Optional[int] = None
    unit_price: Optional[int] = None
    bid: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Auction':
        assert isinstance(obj, dict)
        id = from_int(obj.get("id"))
        item = Item.from_dict(obj.get("item"))
        quantity = from_int(obj.get("quantity"))
        time_left = TimeLeft(obj.get("time_left"))
        buyout = from_union([from_int, from_none], obj.get("buyout"))
        unit_price = from_union([from_int, from_none], obj.get("unit_price"))
        bid = from_union([from_int, from_none], obj.get("bid"))
        return Auction(id, item, quantity, time_left, buyout, unit_price, bid)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_int(self.id)
        result["item"] = to_class(Item, self.item)
        result["quantity"] = from_int(self.quantity)
        result["time_left"] = to_enum(TimeLeft, self.time_left)
        result["buyout"] = from_union([from_int, from_none], self.buyout)
        result["unit_price"] = from_union([from_int, from_none], self.unit_price)
        result["bid"] = from_union([from_int, from_none], self.bid)
        return result


@dataclass
class ConnectedRealm:
    href: str

    @staticmethod
    def from_dict(obj: Any) -> 'ConnectedRealm':
        assert isinstance(obj, dict)
        href = from_str(obj.get("href"))
        return ConnectedRealm(href)

    def to_dict(self) -> dict:
        result: dict = {}
        result["href"] = from_str(self.href)
        return result


@dataclass
class Links:
    links_self: ConnectedRealm

    @staticmethod
    def from_dict(obj: Any) -> 'Links':
        assert isinstance(obj, dict)
        links_self = ConnectedRealm.from_dict(obj.get("self"))
        return Links(links_self)

    def to_dict(self) -> dict:
        result: dict = {}
        result["self"] = to_class(ConnectedRealm, self.links_self)
        return result


@dataclass
class GetAuction:
    links: Links
    connected_realm: ConnectedRealm
    auctions: List[Auction]

    @staticmethod
    def from_dict(obj: Any) -> 'GetAuction':
        assert isinstance(obj, dict)
        links = Links.from_dict(obj.get("_links"))
        connected_realm = ConnectedRealm.from_dict(obj.get("connected_realm"))
        auctions = from_list(Auction.from_dict, obj.get("auctions"))
        return GetAuction(links, connected_realm, auctions)

    def to_dict(self) -> dict:
        result: dict = {}
        result["_links"] = to_class(Links, self.links)
        result["connected_realm"] = to_class(ConnectedRealm, self.connected_realm)
        result["auctions"] = from_list(lambda x: to_class(Auction, x), self.auctions)
        return result


def get_auction_from_dict(s: Any) -> GetAuction:
    return GetAuction.from_dict(s)


def get_auction_to_dict(x: GetAuction) -> Any:
    return to_class(GetAuction, x)
