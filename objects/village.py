from gen.village.neighbourhood_amount import get_neighbourhood_amount
from objects.neighbourhood import Neighbourhood
from src.cache import cached_property

class Village:
    def __init__(self, name, size, password):
        self.name = name
        self.size = size
        self.seed = (password, name, size)

    @cached_property
    def neighbourhood_amount(self):
        return get_neighbourhood_amount(self.seed+('neighbourhood-amount',), self.size)
    
    @cached_property
    def neighbourhoods(self):
        return [Neighbourhood(self.seed + (i,), self) for i in range(self.neighbourhood_amount)]
    
    def find(self, obj_type, seed):
        if len(seed) < 3:
            return None
        elif len(seed) == 3:
            return self if (seed == self.seed and obj_type == 'village') else None
        else:
            num = int(seed[3])
            try:
                neighbourhood = self.neighbourhoods[num]
            except IndexError:
                return None
            else:
                return neighbourhood.find(obj_type, seed)                