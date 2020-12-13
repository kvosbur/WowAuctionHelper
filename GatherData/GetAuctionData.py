import json
import Models
from Models import auction
from Database.auction import add_all_auctions
from GatherData import apiObj, region, static_ns, locale, realm_id


def get_auction_data():
    b = apiObj.get_auctions(region, 'dynamic-us', connected_realm_id=realm_id)

    parsed = auction.get_auction_from_dict(b)
    add_all_auctions(parsed)

