from dataclasses import dataclass
from typing import Any, Optional, List, TypeVar, Callable, Type, cast
from enum import Enum
from Models.helpers import *

@dataclass
class Self:
    href: str

    @staticmethod
    def from_dict(obj: Any) -> 'Self':
        assert isinstance(obj, dict)
        href = from_str(obj.get("href"))
        return Self(href)

    def to_dict(self) -> dict:
        result: dict = {}
        result["href"] = from_str(self.href)
        return result


@dataclass
class ItemClass:
    key: Self
    name: str
    id: int

    @staticmethod
    def from_dict(obj: Any) -> 'ItemClass':
        assert isinstance(obj, dict)
        key = Self.from_dict(obj.get("key"))
        name = from_str(obj.get("name"))
        id = from_int(obj.get("id"))
        return ItemClass(key, name, id)

    def to_dict(self) -> dict:
        result: dict = {}
        result["key"] = to_class(Self, self.key)
        result["name"] = from_str(self.name)
        result["id"] = from_int(self.id)
        return result


@dataclass
class Links:
    links_self: Self

    @staticmethod
    def from_dict(obj: Any) -> 'Links':
        assert isinstance(obj, dict)
        links_self = Self.from_dict(obj.get("self"))
        return Links(links_self)

    def to_dict(self) -> dict:
        result: dict = {}
        result["self"] = to_class(Self, self.links_self)
        return result


@dataclass
class GetItemClassData:
    links: Links
    item_classes: List[ItemClass]

    @staticmethod
    def from_dict(obj: Any) -> 'GetItemClassData':
        assert isinstance(obj, dict)
        links = Links.from_dict(obj.get("_links"))
        item_classes = from_list(ItemClass.from_dict, obj.get("item_classes"))
        return GetItemClassData(links, item_classes)

    def to_dict(self) -> dict:
        result: dict = {}
        result["_links"] = to_class(Links, self.links)
        result["item_classes"] = from_list(lambda x: to_class(ItemClass, x), self.item_classes)
        return result


def get_item_class_data_from_dict(s: Any) -> GetItemClassData:
    return GetItemClassData.from_dict(s)


def get_item_class_data_to_dict(x: GetItemClassData) -> Any:
    return to_class(GetItemClassData, x)