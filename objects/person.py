from gen.person import (
    name,
    inventory,
    level
)
from src.cache import cached_property
from gen.house import schedule

class Person:
    def __init__(self, seed, house):
        self.seed = seed
        self.house = house
        self.fi = seed[-1]      # Family Index

        self.race = house.race
        self.gender = house.genders[self.fi]

        self.is_mature = (self.fi < 2)
    
    @cached_property
    def class_name(self):
        if self.fi > 0:
            return 'Commoner'
        else:
            return self.house.occupation

    @cached_property
    def name(self):
        return name.first_name(self.seed + ('name',), self.race, self.gender) + ' ' + self.house.family_name
    
    @cached_property
    def inventory(self):
        return inventory.get_inventory(self.seed + ('inventory',))

    @cached_property
    def level(self):
        return level.get_level(self.seed + ('level',), self.class_name, self.is_mature)

    @cached_property
    def schedule(self):
        return schedule.translate_schedule(self.house.schedule, self.is_mature, self.house.neighbourhood.houses['Barkeep'][0].name)
    

    def find(self, obj_type, seed):
        return self if (seed == self.seed and obj_type == 'person') else None