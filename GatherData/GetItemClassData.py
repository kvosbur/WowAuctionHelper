from Models import itemclass, itemsubclass
from Database.item import addAllItemClassToDb, addAllItemSubClassToDb
from GatherData import apiObj, region, static_ns, locale, realm_id


def get_item_class_data():

    classes_raw = apiObj.get_item_class_index(region, static_ns, locale=locale)
    classes = itemclass.get_item_class_data_from_dict(classes_raw)
    addAllItemClassToDb(classes)

    for c in classes.item_classes:
        item_class_data_raw = apiObj.get_item_class(region, static_ns, c.id, locale=locale)
        item_class_data = itemsubclass.get_item_sub_class_data_from_dict(item_class_data_raw)
        addAllItemSubClassToDb(c.id, item_class_data)
