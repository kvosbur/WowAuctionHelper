from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

from DBModels import Item
from DBModels import Auction, Dungeon
from DBModels import Encounter
from DBModels import EncounterItems, Ingredient
from DBModels import ItemClass, ItemSubClass, Media
from DBModels import Profession, Rank, Recipe
from DBModels import PlayerClass
from DBModels import PlayerClassSpecialization
from DBModels import AzeriteTrait
from DBModels import ClassSpecializationAzeriteRelation
from DBModels import AzeriteItem


