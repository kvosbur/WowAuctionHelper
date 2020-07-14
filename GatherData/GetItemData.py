from GatherData import apiObj, region, locale
import json


def get_item_data(item_id):
    return apiObj.get_item_data(region, "static-8.3.0_32861-us", item_id, locale=locale)
