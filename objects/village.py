from gen.village.neighbourhood_amount import get_neighbourhood_amount
from objects.neighbourhood import Neighbourhood
from src.cache import cached_property
import json

with open('data/occupations.json', 'r') as open_file:
    occup_dic = json.load(open_file)
    CLASS_WITH_COMMONERS = [occup for occup in occup_dic if occup_dic[occup]['family'] or occup == 'Commoner']

class Village:
    def __init__(self, name, size, password):
        self.name = name
        self.size = size
        self.seed = (password, name, size)

    @cached_property
    def classes(self):
        with open('data/occupations.json', 'r') as open_file:
            occupations = json.load(open_file)

            c = {
                o: {
                    'total': sum([n.house_amounts[o] for n in self.neighbourhoods]),
                    'shop': occupations[o]['shop']
                }
                for o in occupations
            }
        
        for o in CLASS_WITH_COMMONERS:
            for n in self.neighbourhoods:
                for h in n.houses[o]:
                    c['Commoner']['total'] += h.inhabitant_amount - 1
        return c

    @cached_property
    def neighbourhood_amount(self):
        return get_neighbourhood_amount(self.seed+('neighbourhood-amount',), self.size)
    
    @cached_property
    def neighbourhoods(self):
        return [Neighbourhood(self.seed + (i,), self) for i in range(self.neighbourhood_amount)]
    
    def iter_houses(self, house_type, maximum=0):
        def house_gen():
            for n in self.neighbourhoods:
                try:
                    for house in n.houses[house_type]:
                        yield house
                except KeyError:
                    break
        
        if maximum == 0:
            return [house for house in house_gen()]
        else:
            return [house for house, _ in zip(house_gen(), range(maximum))]
    
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