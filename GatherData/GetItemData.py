from GatherData import apiObj, region, locale
from Models import character


def get_item_data(item_id):
    try:
        return apiObj.get_item_data(region, "static-us", item_id, locale=locale)
    except:
        print('error for: ', item_id)
        return None


def get_char_prof_summary(character_name):
    temp = apiObj.get_character_profile_summary(region, "profile-us", "wyrmrest-accord", character_name.lower(),
                                                locale=locale)

    character_class = temp["character_class"]["id"]
    character_spec = temp["active_spec"]["id"]
    guild_name = temp["guild"]["name"]
    guild_id = temp["guild"]["id"]
    return {"class_id": character_class, "spec_id": character_spec, "guild_name": guild_name,
            "guild_id": guild_id}


def get_equipment_for_character(character_name):
    temp = apiObj.get_character_equipment_summary(region, "profile-us", "wyrmrest-accord", character_name.lower(),
                                                  locale=locale)
    print(str(temp).replace("'", '"'))
    more_info = get_char_prof_summary(character_name)

    char_obj = character.Character(character_name, **more_info)

    for item in temp["equipped_items"]:
        slot_type = item["slot"]["type"]
        ilvl = item["level"]["value"]
        char_obj.add_item(slot_type, ilvl)

    return char_obj