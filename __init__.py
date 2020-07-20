

import os
from dotenv import load_dotenv
base_directory = os.path.dirname(os.path.abspath(__file__))
env_file_path = os.path.join(base_directory, ".env")
load_dotenv(env_file_path)

from Database import item, mythic
from GatherData import GetAuctionData, GetDungeonData, GetItemData, GetItemClassData
from websrc import app


def add_data_to_db():
    GetItemClassData.get_item_class_data()

    res = GetDungeonData.getMythicData()
    mythic.addAllDungeons(res)
    o = GetDungeonData.getEncounters(res)
    mythic.addAllEncounters(o)
    out = GetDungeonData.getItemsFromEncounters(o)
    mythic.addAllEncounterItems(out)


if __name__ == "__main__":
    # azerite 155860
    # normal piece 158371
    a = 3


    #app.run()
