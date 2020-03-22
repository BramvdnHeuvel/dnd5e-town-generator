from gen.neighbourhood.house_amounts import house_amounts
from src.cache import cached_property
from objects.house import House

class Neighbourhood:
    def __init__(self, seed, village):
        self.seed = seed
        self.village = village
    
    @cached_property
    def house_amounts(self):
        return house_amounts(self.seed)
    
    @cached_property
    def houses(self):
        return {
            occupation: [
                House(self.seed + (occupation, i), self) for i in range(self.house_amounts[occupation])
            ]
            for occupation in self.house_amounts
        }
    
    def find(self, obj_type, seed):
        if len(seed) == 4:
            return self if (seed == self.seed and obj_type == 'neighbourhood') else None
        elif len(seed) == 5:
            return None
        else:
            if seed[4] in self.houses:
                try:
                    house = self.houses[seed[4]][int(seed[5])]
                except IndexError:
                    return None
                else:
                    return house.find(obj_type, seed)
            else:
                return None
