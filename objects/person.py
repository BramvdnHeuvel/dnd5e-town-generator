from gen.person import (
    name,
    inventory,
    level,
    commoner_occupation
)
from src.cache import cached_property
from gen.house import schedule
from flask import url_for

class Person:
    def __init__(self, seed, house):
        self.seed = seed
        self.house = house
        self.fi = seed[-1]      # Family Index

        self.race = house.race
        self.gender = house.genders[self.fi]

        self.is_mature = (self.fi < 2)
    
    def __html__(self):
        return f'<a href="{url_for("get_npc", **self.url_package)}">{self.name}</a>'

    @cached_property
    def url_package(self):
        return {
            'town_name': self.seed[1],
            'size': self.seed[2],
            'neighbourhood': self.seed[3],
            'class_name': self.seed[4],
            'house': self.seed[5],
            'person': self.seed[6]
        }

    @cached_property
    def age(self):
        return self.house.ages[self.fi]
    
    @cached_property
    def class_name(self):
        if self.fi > 0:
            return 'Commoner'
        else:
            return self.house.occupation
    
    @cached_property
    def fancy_class_name(self):
        if self.class_name == 'Commoner' and self.fi == 0:
            return commoner_occupation.get_occupation(self.seed + ('fancy_occupation',))
        return self.class_name

    @cached_property
    def name(self):
        return name.first_name(self.seed + ('name',), self.race, self.gender) + ' ' + self.house.family_name
    
    @cached_property
    def inventory(self):
        return inventory.get_inventory(self.seed + ('inventory',), self.is_mature)

    @cached_property
    def level(self):
        return level.get_level(self.seed + ('level',), self.class_name, self.is_mature)

    @cached_property
    def schedule(self):
        return schedule.translate_schedule(self.house.family_schedule, self.is_mature, self.house.neighbourhood.houses['Barkeep'][0].extra_data['link'])
    

    def find(self, obj_type, seed):
        return self if (seed == self.seed and obj_type == 'person') else None