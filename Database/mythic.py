from Database import session
from DBModels import Dungeon, Encounter, EncounterItems
from Database.item import addItemById


def addAllDungeons(mythic_dung_data):
    for dung in mythic_dung_data:
        dung_name, journal_id, mythic_id = dung
        dungeon_inst = Dungeon.Dungeon(mythic_id, journal_id, dung_name)
        session.add(dungeon_inst)
    session.commit()


def addAllEncounters(encounter_data):
    for journal_id, encounters in encounter_data.items():
        for encounter in encounters:
            encounter_name, encounter_id = encounter
            encount_obj = Encounter.Encounter(encounter_id, journal_id, encounter_name)
            session.add(encount_obj)
    session.commit()


def addAllEncounterItems(encounter_items_data):
    for encounter_id, encounter_items in encounter_items_data.items():
        for encounter_item in encounter_items:
            item_id, item_name = encounter_item
            addItemById(item_id)
            encount_item_obj = EncounterItems.EncounterItems(encounter_id, item_id)
            session.add(encount_item_obj)
    session.commit()

