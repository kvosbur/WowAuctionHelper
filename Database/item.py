from Database import session
from DBModels import Item, ItemClass, ItemSubClass, Media
from Models import itemclass, itemsubclass
from typing import List
from GatherData.GetItemData import get_item_data


def addAllItemClassToDb(item_class_data: List[itemclass.ItemClass]):
    for c in item_class_data.item_classes:
        item_name = c.name
        item_id = c.id
        item_class = ItemClass.ItemClass(item_id, item_name)

        session.add(item_class)
    session.commit()


def addAllItemSubClassToDb(item_class_id: int, item_subclass_data: List[itemsubclass.ItemSubclass]):
    for sub in item_subclass_data.item_subclasses:
        item_subclass = ItemSubClass.ItemSubClass(sub.id, item_class_id, sub.name)
        session.add(item_subclass)
    session.commit()


def addItemById(item_id):
    data = get_item_data(item_id)
    addItemToDb(data)


def addMedia(media_url, media_id):
    if session.query(Media.Media).filter(Media.Media.mediaId == media_id).first() is not None:
        return
    media_obj = Media.Media(media_id, media_url)
    session.add(media_obj)
    session.commit()


def organizeStats(raw_stats):
    ret = {}
    for stat in raw_stats:
        if stat["type"]["type"] in Item.Stats:
            ret[Item.Stats[stat["type"]["type"]]] = 1
    return ret


def addItemToDb(item_json_data):
    item_id = item_json_data["id"]
    if session.query(Item.Item).filter(Item.Item.itemId == item_id).first() is not None:
        return
    print("item", item_id)
    item_name = item_json_data["name"]
    item_media_id = item_json_data["media"]["id"]
    item_media_url = item_json_data["media"]["key"]["href"]
    addMedia(item_media_url, item_media_id)
    item_class = item_json_data["item_class"]["id"]
    item_subclass = item_json_data["item_subclass"]["id"]
    item_inventory_type = item_json_data["inventory_type"]["name"]

    stat_dict = {}
    if "stats" in item_json_data["preview_item"].keys():
        stat_dict = organizeStats(item_json_data["preview_item"]["stats"])
    item = Item.Item(item_id, item_class, item_subclass, item_name, item_media_id, item_inventory_type, **stat_dict)
    session.add(item)
    session.commit()
