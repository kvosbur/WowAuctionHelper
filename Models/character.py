

class Character:
    ITEM_TYPES = ["HEAD", "NECK", "SHOULDER", "CHEST", "WAIST", "LEGS", "FEET", "WRIST", "HANDS",
                  "FINGER_1", "FINGER_2", "TRINKET_1", "TRINKET_2", "BACK", "MAIN_HAND", "OFF_HAND"]

    def __init__(self, name):
        self.name = name
        self.items = {}

    def add_item(self, type, item_lvl):
        if type in Character.ITEM_TYPES:
            self.items[type] = item_lvl