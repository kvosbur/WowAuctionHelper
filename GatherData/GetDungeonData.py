
from GatherData import apiObj, region, dynamic_ns, locale, realm_id, static_ns

def getMythicData():
    res = apiObj.get_mythic_keystone_dungeon_index(region=region, namespace=dynamic_ns, locale=locale)
    dungeons = [(x["name"], x["id"]) for x in res['dungeons']]

    journal_data = []
    for d in dungeons:
        raw_data = apiObj.get_mythic_keystone_dungeon(region, dynamic_ns, d[1], locale=locale)
        journal_data.append((d[0], raw_data["dungeon"]["id"], d[1]))

    return journal_data


def getEncounters(mythicData):
    encounters = {}
    for dung in mythicData:
        raw_data = apiObj.get_journal_instance(region, static_ns, dung[1], locale=locale)
        current = [(x["name"], x["id"]) for x in raw_data["encounters"]]
        encounters[dung[1]] = current

    return encounters


def getItemsFromEncounters(encounterData):
    encounters = {}
    for key, value in encounterData.items():
        for encounter in value:
            items = []
            raw_data = apiObj.get_journal_encounter(region, static_ns, encounter[1], locale=locale)
            for item in raw_data["items"]:
                item_name = item["item"]["name"]
                item_id = item["item"]["id"]
                items.append((item_id, item_name))
            encounters[encounter[1]] = items
    return encounters