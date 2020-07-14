

import os
from dotenv import load_dotenv
base_directory = os.path.dirname(os.path.abspath(__file__))
env_file_path = os.path.join(base_directory, ".env")
load_dotenv(env_file_path)

from Database import item, mythic
from GatherData import GetAuctionData, GetDungeonData, GetItemData, GetItemClassData
from websrc import app



if __name__ == "__main__":


    GetItemClassData.get_item_class_data()

    res = GetDungeonData.getMythicData()
    mythic.addAllDungeons(res)
    o = GetDungeonData.getEncounters(res)
    mythic.addAllEncounters(o)
    out = GetDungeonData.getItemsFromEncounters(o)
    mythic.addAllEncounterItems(out)



    # azerite 155860
    # normal piece 158371
    res = GetItemData.get_item_data(158371)
    '''
    temp = res["azerite_class_powers"]
    for i in temp:
        print(i)
        print(i["playable_class"])
    '''

    # 158371
    for x in res["preview_item"]["stats"]:
        print(x)

    #item.addItemToDb(res)



    #app.run()
