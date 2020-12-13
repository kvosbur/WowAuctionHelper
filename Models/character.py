

class Character:
    ITEM_TYPES = ["HEAD", "NECK", "SHOULDER", "CHEST", "WAIST", "LEGS", "FEET", "WRIST", "HANDS",
                  "FINGER_1", "FINGER_2", "TRINKET_1", "TRINKET_2", "BACK", "MAIN_HAND", "OFF_HAND"]

    armor_type = {"Plate": ["Warrior", "Paladin", "Death Knight", "Demon Hunter"],
                  "Mail": ["Hunter", "Shaman"],
                  "Leather": ["Rogue", "Monk", "Druid"],
                  "Cloth": ["Priest", "Warlock", "Mage"]}

    intellect = "INTELLECT"
    agi = "AGILITY"
    strength = "STRENGTH"

    primary_stats = {"INTELLECT": ["Mage", "Warlock", "Priest", {"Druid": ["Restoration", "Balance"]},
                                   {"Monk": ["Mistweaver"]}, {"Shaman": ["Elemental", "Restoration"]},
                                   {"Paladin": ["Holy"]}],
                     "AGILITY": ["Demon Hunter", {"Druid": ["Feral", "Guardian"]}, "Rogue", {"Monk": ["Brewmaster, Windwalker"]},
                                 "Hunter", {"Shaman": ["Enhancement"]}],
                     "STRENGTH": ["Death Knight", {"Paladin": ["Retribution", "Protection"]},
                                  "Warrior"]}

    allowed_weapons = {
        "One-Handed Axes": ["Death Knight", "Demon Hunter", "Hunter", "Monk", "Paladin", {"Rogue": ["Outlaw"]}, "Shaman", "Warrior"],
        "Two-Handed Axes": ["Death Knight", "Hunter", "Paladin", "Shaman", "Warrior"],
        "Bows": ["Hunter", "Warrior"],
        "Guns": ["Hunter", "Warrior"],
        "One-Handed Maces": ["Death Knight", "Monk", "Paladin", "Priest", {"Rogue": ["Outlaw"]}, "Shaman", "Warrior"],
        "Two-Handed Maces": ["Death Knight", "Paladin", "Shaman", "Warrior"],
        "Polearms": ["Death Knight", "Hunter", "Monk", "Paladin", "Warrior"],
        "One-Handed Swords": ["Death Knight", "Demon Hunter", "Hunter", "Mage", "Monk", "Paladin", {"Rogue": ["Outlaw"]}, "Warlock", "Warrior"],
        "Two-Handed Swords": ["Death Knight", "Hunter", "Paladin", "Warrior"],
        "Warglaives": ["Demon Hunter"],
        "Staves": ["Hunter", "Mage", "Monk", "Priest", "Shaman", "Warlock", "Warrior"],
        "Bear Claws": [],
        "CatClaws": [],
        "Fist Weapons": ["Demon Hunter", "Hunter", "Monk", {"Rogue": ["Outlaw"]}, "Shaman", "Warrior"],
        "Miscellaneous": [],
        "Daggers": ["Hunter", "Mage", "Priest", {"Rogue": ["Assassination", "Subtle", "Outlaw"]}, "Shaman", "Warlock", "Warrior"],
        "Thrown": [{"Rogue": ["Outlaw"]}, "Warrior"],
        "Spears": [],
        "Crossbows": ["Hunter", "Warrior"],
        "Wands": ["Mage", "Priest", "Warlock"]
    }


    # these are for shield, Miscellaneous (inventory type = HOLDABLE
    specific_allowed = {}

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