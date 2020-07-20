from Database import session
from DBModels import Item, ItemClass, ItemSubClass, Media, PlayerClass, PlayerClassSpecialization
from DBModels import AzeriteTrait, ClassSpecializationAzeriteRelation, AzeriteItem
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


def addPlayerClassIfNotPresent(class_name, class_id):
    if session.query(PlayerClass.PlayerClass).filter(PlayerClass.PlayerClass.playerClassId == class_id).first() is not None:
        return
    player_class_obj = PlayerClass.PlayerClass(class_id, class_name)
    session.add(player_class_obj)
    session.commit()


def addPlayerClassSpecializationIfNotPresent(class_id, spec_id, spec_name):
    if session.query(PlayerClassSpecialization.PlayerClassSpecialization).filter(
            PlayerClassSpecialization.PlayerClassSpecialization.playerClassSpecId == spec_id).first() is not None:
        return
    spec_class_obj = PlayerClassSpecialization.PlayerClassSpecialization(spec_id, class_id, spec_name)
    session.add(spec_class_obj)
    session.commit()


def addAzeriteTraitsForClass(item_id, traits_json, player_class_id):
    for trait in traits_json:
        power_id = trait["spell"]["id"]
        if session.query(AzeriteTrait.AzeriteTrait).filter(
                AzeriteTrait.AzeriteTrait.power_id == power_id).first() is not None:
            return

        tier = trait["tier"]
        name = trait["spell"]["name"]
        azerite_obj = AzeriteTrait.AzeriteTrait(power_id, tier, name, player_class_id)
        session.add(azerite_obj)

        session.commit()

        if "allowed_specializations" in trait:
            for spec in trait["allowed_specializations"]:
                player_class_spec_id = spec["id"]
                player_class_spec_name = spec["name"]
                addPlayerClassSpecializationIfNotPresent(player_class_id, player_class_spec_id, player_class_spec_name)
                relation = ClassSpecializationAzeriteRelation.AzeriteClassSpecialization(player_class_spec_id, power_id)
                session.add(relation)

        azerite_item_obj = AzeriteItem.AzeriteItem(item_id, power_id)
        session.add(azerite_item_obj)
        session.commit()

def addAzeriteTraits(raw_json, item_id):
    for traits in raw_json:
        # setup player class
        player_class_name = traits["playable_class"]["name"]
        player_class_id = traits["playable_class"]["id"]
        addPlayerClassIfNotPresent(player_class_name, player_class_id)
        addAzeriteTraitsForClass(item_id, traits["powers"], player_class_id)


def addItemToDb(item_json_data):
    item_id = item_json_data["id"]
    if session.query(Item.Item).filter(Item.Item.itemId == item_id).first() is not None:
        return
    print(item_id)
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

    if "azerite_class_powers" in item_json_data:
        addAzeriteTraits(item_json_data["azerite_class_powers"], item_id)

    session.commit()
