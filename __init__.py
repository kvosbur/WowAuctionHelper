

import os
from dotenv import load_dotenv
base_directory = os.path.dirname(os.path.abspath(__file__))
env_file_path = os.path.join(base_directory, ".env")
load_dotenv(env_file_path)
import time

from Database import item, mythic
from GatherData import GetAuctionData, GetDungeonData, GetItemData, GetItemClassData
from websrc import app
import argparse


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


def init_argument_parser():
    parser = argparse.ArgumentParser(description='Wow Auction Utility')
    parser.add_argument('--update-data', action='store_true')
    parser.add_argument('--run-webserver', action='store_true')

    return parser


if __name__ == "__main__":
    # azerite 155860
    # normal piece 158371
    # add_instance_info_to_db()
    arguments = init_argument_parser().parse_args()

    if arguments.update_data:
        start = time.time()
        get_auction_info()
        end = time.time()
        print(end - start)

    if arguments.run_webserver:
        app.run()

    #temp = GetItemData.get_equipment_for_character("Ithenis")
    #print(temp)
    #item.getAllAzeriteTraits(temp)

