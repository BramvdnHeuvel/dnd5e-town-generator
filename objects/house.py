from gen.house import (
    age,
    genders,
    inhabitant_amount,
    name,
    race,
    schedule,
    type_data
)
from objects.person import Person
from gen.person.name import last_name
from src.cache import cached_property

class House:
    def __init__(self, seed, neighbourhood):
        self.seed = seed
        self.occupation = seed[-2]
        self.neighbourhood = neighbourhood

    @cached_property
    def ages(self):
        return age.get_ages(self.seed + ('ages',), self.inhabitant_amount, self.race)
    
    @cached_property
    def family_name(self):
        return last_name(self.seed + ('family-name',), self.race)
    
    @cached_property
    def family_schedule(self):
        return schedule.get_schedule(self.seed + ('schedule',), self.occupation=='Tavern')

    @cached_property
    def genders(self):
        return genders.get_genders(self.seed + ('genders', ), self.inhabitant_amount)

    @cached_property
    def inhabitant_amount(self):
        return inhabitant_amount.get_inhabitants(self.seed + ('inhabitant-amount',), self.occupation, self.race)
    
    @cached_property
    def inhabitants(self):
        return [Person(self.seed + (i,), self) for i in range(self.inhabitant_amount)]
    
    @cached_property
    def name(self):     # House name in case the house is also a shop
        return name.get_house_name(self.seed + ('name',))
    
    @cached_property
    def race(self):
        return race.race(self.seed + ('race',))

    def find(self, obj_type, seed):
        if len(seed) == 6:
            return self if (seed == self.seed and obj_type == 'house') else None
        else:
            num = int(seed[6])
            try:
                person = self.inhabitants[num]
            except IndexError:
                return None
            else:
                return person.find(obj_type, seed)
