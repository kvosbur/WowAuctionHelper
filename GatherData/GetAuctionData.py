import json
import Models
from Models import auction
from GatherData import apiObj, region, namespace, locale, realm_id


def get_auction_data():
    b = apiObj.get_auctions(region, namespace, connected_realm_id=realm_id)

    return auction.get_auction_from_dict(b)


def insert_auction_data(auction_data: auction.GetAuction):
    for auc in auction_data.auctions:
        print("hello")
