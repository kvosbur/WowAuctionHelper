

class Character:
    ITEM_TYPES = ["HEAD", "NECK", "SHOULDER", "CHEST", "WAIST", "LEGS", "FEET", "WRIST", "HANDS",
                  "FINGER_1", "FINGER_2", "TRINKET_1", "TRINKET_2", "BACK", "MAIN_HAND", "OFF_HAND"]

    def __init__(self, name, class_id, spec_id, guild_name, guild_id):
        self.name = name
        self.class_id = class_id
        self.spec_id = spec_id
        self.guild_id = guild_id
        self.guild_name = guild_name
        self.items = {}

    def add_item(self, type, item_lvl):
        if type in Character.ITEM_TYPES:
            self.items[type] = item_lvl

    def __repr__(self):
        ret = self.name + " of " + self.guild_name + "\n"
        for x,y in self.items.items():
            ret += x + ": " + str(y) + "\n"
        return ret