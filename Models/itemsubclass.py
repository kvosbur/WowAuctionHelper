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
class ItemSubclass:
    key: Self
    name: str
    id: int

    @staticmethod
    def from_dict(obj: Any) -> 'ItemSubclass':
        assert isinstance(obj, dict)
        key = Self.from_dict(obj.get("key"))
        name = from_str(obj.get("name"))
        id = from_int(obj.get("id"))
        return ItemSubclass(key, name, id)

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
class GetItemSubClassData:
    links: Links
    class_id: int
    name: str
    item_subclasses: List[ItemSubclass]

    @staticmethod
    def from_dict(obj: Any) -> 'GetItemSubClassData':
        assert isinstance(obj, dict)
        links = Links.from_dict(obj.get("_links"))
        class_id = from_int(obj.get("class_id"))
        name = from_str(obj.get("name"))
        item_subclasses = from_list(ItemSubclass.from_dict, obj.get("item_subclasses"))
        return GetItemSubClassData(links, class_id, name, item_subclasses)

    def to_dict(self) -> dict:
        result: dict = {}
        result["_links"] = to_class(Links, self.links)
        result["class_id"] = from_int(self.class_id)
        result["name"] = from_str(self.name)
        result["item_subclasses"] = from_list(lambda x: to_class(ItemSubclass, x), self.item_subclasses)
        return result


def get_item_sub_class_data_from_dict(s: Any) -> GetItemSubClassData:
    return GetItemSubClassData.from_dict(s)


def get_item_sub_class_data_to_dict(x: GetItemSubClassData) -> Any:
    return to_class(GetItemSubClassData, x)
