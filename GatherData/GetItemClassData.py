from Models import itemclass, itemsubclass
from Database.item import addAllItemClassToDb, addItemSubClassToDb
from GatherData import apiObj, region, static_ns, locale, realm_id


def get_item_class_data():

    classes_raw = apiObj.get_item_class_index(region, static_ns, locale=locale)
    classes = itemclass.get_item_class_data_from_dict(classes_raw)
    addAllItemClassToDb(classes)

    for c in classes.item_classes:
        item_class_data_raw = apiObj.get_item_class(region, static_ns, c.id, locale=locale)
        item_class_data = itemsubclass.get_item_sub_class_data_from_dict(item_class_data_raw)
        class_id = c.id
        for sub in item_class_data.item_subclasses:
            item_subclass_data = apiObj.get_item_subclass(region, static_ns, c.id, sub.id, locale=locale )
            subclass_id = sub.id
            sub_class_name = item_subclass_data["display_name"]
            if "verbose_name" in item_subclass_data:
                sub_class_name = item_subclass_data["verbose_name"]
            addItemSubClassToDb(class_id, subclass_id, sub_class_name)
