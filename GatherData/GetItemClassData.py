from Models import itemclass, itemsubclass
from GatherData import apiObj, region, namespace, locale, realm_id

classes_raw = apiObj.get_item_class_index(region, namespace, locale=locale)
classes = itemclass.get_item_class_data_from_dict(classes_raw)


for c in classes.item_classes:
    item_class_data_raw = apiObj.get_item_class(region, namespace, c.id, locale=locale)
    item_class_data = itemsubclass.get_item_sub_class_data_from_dict(item_class_data_raw)
    print("---" + item_class_data.name)
    for subclass in item_class_data.item_subclasses:
        print(subclass.name)
