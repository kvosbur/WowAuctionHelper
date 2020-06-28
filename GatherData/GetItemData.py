from GatherData import apiObj, region, namespace, locale
import json


def get_item_data(item_id):
    return apiObj.get_item_data(region, namespace, item_id, locale=locale)
