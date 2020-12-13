

import os
from dotenv import load_dotenv
base_directory = os.path.dirname(os.path.abspath(__file__))
env_file_path = os.path.join(base_directory, ".env")
load_dotenv(env_file_path)
import time

from Database import item, mythic
from GatherData import GetAuctionData, GetDungeonData, GetItemData, GetItemClassData
from websrc import app


def add_instance_info_to_db():
    GetItemClassData.get_item_class_data()

    res = GetDungeonData.getMythicData()
    mythic.addAllDungeons(res)
    o = GetDungeonData.getEncounters(res)
    mythic.addAllEncounters(o)
    out = GetDungeonData.getItemsFromEncounters(o)
    mythic.addAllEncounterItems(out)


def get_auction_info():
    t = GetAuctionData.get_auction_data()


if __name__ == "__main__":
    # azerite 155860
    # normal piece 158371
    # add_instance_info_to_db()

    #start = time.time()
    #get_auction_info()
    #end = time.time()
    #print(end - start)

    #temp = GetItemData.get_equipment_for_character("Ithenis")
    #print(temp)
    #item.getAllAzeriteTraits(temp)
    app.run()
