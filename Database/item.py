from Database import session
from DBModels.Item import Item, Stats
from DBModels.ItemClass import ItemClass
from DBModels.ItemSubClass import ItemSubClass
from DBModels.Media import Media
from DBModels.PlayerClass import PlayerClass
from DBModels.PlayerClassSpecialization import PlayerClassSpecialization
from DBModels.AzeriteTrait import AzeriteTrait
from DBModels.ClassSpecializationAzeriteRelation import AzeriteClassSpecialization
from DBModels.AzeriteItem import AzeriteItem
from Models import itemclass, itemsubclass
from typing import List
from GatherData.GetItemData import get_item_data
from sqlalchemy import func


def addAllItemClassToDb(item_class_data: List[itemclass.ItemClass]):
    for c in item_class_data.item_classes:
        item_name = c.name
        item_id = c.id
        item_class = ItemClass(item_id, item_name)

        session.add(item_class)
    session.commit()


def addItemSubClassToDb(item_class_id: int, item_subclass_id: int, item_subclass_name: str):
    item_subclass = ItemSubClass(item_subclass_id, item_class_id, item_subclass_name)
    session.add(item_subclass)
    session.commit()


def addItemById(item_id):
    if session.query(Item).filter(Item.itemId == item_id).first() is not None:
        return item_id
    data = get_item_data(item_id)
    if data is not None:
        addItemToDb(data)
        return item_id
    return None


def addMedia(media_url, media_id):
    if session.query(Media).filter(Media.mediaId == media_id).first() is not None:
        return
    media_obj = Media(media_id, media_url)
    session.add(media_obj)
    session.commit()


def organizeStats(raw_stats):
    ret = {}
    for stat in raw_stats:
        if "type" in stat and stat["type"]["type"] in Stats:
            ret[Stats[stat["type"]["type"]]] = 1
    return ret


def addPlayerClassIfNotPresent(class_name, class_id):
    if session.query(PlayerClass).filter(PlayerClass.playerClassId == class_id).first() is not None:
        return
    player_class_obj = PlayerClass(class_id, class_name)
    session.add(player_class_obj)
    session.commit()


def addPlayerClassSpecializationIfNotPresent(class_id, spec_id, spec_name):
    if session.query(PlayerClassSpecialization).filter(
            PlayerClassSpecialization.playerClassSpecId == spec_id).first() is not None:
        return
    spec_class_obj = PlayerClassSpecialization(spec_id, class_id, spec_name)
    session.add(spec_class_obj)
    session.commit()


def addAzeriteTraitsForClass(item_id, traits_json, player_class_id):
    for trait in traits_json:
        power_id = trait["spell"]["id"]
        if session.query(AzeriteTrait).filter(
                AzeriteTrait.power_id == power_id).first() is not None:
            return

        tier = trait["tier"]
        name = trait["spell"]["name"]
        azerite_obj = AzeriteTrait(power_id, tier, name, player_class_id)
        session.add(azerite_obj)

        session.commit()

        if "allowed_specializations" in trait:
            for spec in trait["allowed_specializations"]:
                player_class_spec_id = spec["id"]
                player_class_spec_name = spec["name"]
                addPlayerClassSpecializationIfNotPresent(player_class_id, player_class_spec_id, player_class_spec_name)
                relation = AzeriteClassSpecialization(player_class_spec_id, power_id)
                session.add(relation)

        azerite_item_obj = AzeriteItem(item_id, power_id)
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
    if session.query(Item).filter(Item.itemId == item_id).first() is not None:
        return
    item_name = item_json_data["name"]
    item_media_id = item_json_data["media"]["id"]
    item_media_url = item_json_data["media"]["key"]["href"]
    addMedia(item_media_url, item_media_id)
    item_class = item_json_data["item_class"]["id"]
    item_subclass = item_json_data["item_subclass"]["id"]
    item_inventory_type = item_json_data["inventory_type"]["name"]
    item_purchase_price = item_json_data["purchase_price"] if ("purchase_price" in item_json_data) else 0

    stat_dict = {}
    if "stats" in item_json_data["preview_item"].keys():
        try:
            stat_dict = organizeStats(item_json_data["preview_item"]["stats"])
        except:
            print(item_id, item_json_data)
    item = Item(item_id, item_class, item_subclass, item_name, item_media_id, item_inventory_type, item_purchase_price,
                **stat_dict)
    session.add(item)

    if "azerite_class_powers" in item_json_data:
        addAzeriteTraits(item_json_data["azerite_class_powers"], item_id)

    session.commit()


def getAllAzeriteTraits(character_obj):
    overall = session.query(AzeriteTrait, PlayerClass).filter(AzeriteTrait.playerClassId == PlayerClass.playerClassId and
                                                         character_obj.class_id == PlayerClass.playerClassId).all()
    allowed = []
    for item in overall:
        spec_allowed = False
        specificSpecs = session.query(AzeriteClassSpecialization).filter(AzeriteClassSpecialization.power_id == item[0].power_id).all()
        if len(specificSpecs) > 0:
            for spec in specificSpecs:
                if spec.playerClassSpecId == character_obj.spec_id:
                    spec_allowed = True
        else:
            spec_allowed = True

        if spec_allowed:
            allowed.append(item[0])

    # returns list of AzeriteTrait for allowed traits for specified character
    return allowed


def item_exists_by_name(item_name):
    return session.query(Item).filter(func.lower(Item.name) == item_name.lower()).first() is not None


def get_item_by_name(item_name):
    return session.query(Item).filter(func.lower(Item.name) == item_name.lower()).first()
