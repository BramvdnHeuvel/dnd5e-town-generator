import random
from objects.neighbourhood import Neighbourhood
from objects.block import cached_property, NEIGHBOURHOOD_SIZE_TO_RANGE, AVAILABLE_CLASS

class Village:
    def __init__(self, seed, size):
        self.seed = f'{seed}-{size}'
        self.name = seed
        self.size = size

    @cached_property
    def neighbourhood_amount(self):
        random.seed(f'{self.seed}-neighs')
        return random.randint(*NEIGHBOURHOOD_SIZE_TO_RANGE[self.size])
    
    @cached_property
    def neighbourhoods(self):
        total = 0
        n = []

        for i in range(self.neighbourhood_amount):
            neighbourhood = Neighbourhood(f'{self.seed}-{i}', total)
            total += neighbourhood.inhabitants
            n.append(neighbourhood)

        return n
    
    @cached_property
    def classes(self):
        return [clss for clss in self.__available_classes()]
    
    @cached_property
    def inhabitants(self):
        return sum([neighbourhood.inhabitants for neighbourhood in self.neighbourhoods])

    def find_npc(self, number):
        npc = None
        for neighbourhood in self.neighbourhoods:
            npc = neighbourhood.find_npc(number)
            if npc is not None:
                break
        return npc

    def count_class(self, class_name):
        return sum(
            [neighbourhood.house_amounts[f'class-{class_name}'] for neighbourhood in self.neighbourhoods]
        )

    def __available_classes(self):
        for cl in AVAILABLE_CLASS:
            for neigh in self.neighbourhoods:
                if neigh.house_amounts[f'class-{cl}'] > 0:
                    yield cl
                    break

    def iter_over_class(self, class_name, page_number=None):
        if page_number == None:
            for neighbourhood in self.neighbourhoods:
                for house in neighbourhood.houses[f'class-{class_name}']:
                    yield from house.inhabitants

        else:
            page_number = page_number * 50
            people_left = page_number
            skip_to = 0
            people_yielded = 0

            for i in range(self.neighbourhood_amount):
                amount = self.neighbourhoods[i].house_amounts[f'class-{class_name}']
                if amount > people_left:
                    skip_to = i
                    break

                people_left = people_left - amount
            else:
                raise OverflowError("The given page number is too large and does not exist!")

            # Iterate over neighbourhoods, now that the correct starting point has been found.
            for i in range(skip_to, self.neighbourhood_amount):
                neighbourhood = self.neighbourhoods[i]
                
                for j in range(neighbourhood.house_amounts[f'class-{class_name}']):
                    if i == skip_to and j < people_left:
                        continue

                    person = neighbourhood.houses[f'class-{class_name}'][j].inhabitants[0]
                    person.number = page_number + people_yielded
                    yield person
                    people_yielded += 1 # Class houses always have one inhabitant.

                    if people_yielded >= 50:
                        break
                
                if people_yielded >= 50:
                    break

    def get_stores(self, htype, preview=False):
        if preview:
            for house, _ in zip(self.get_stores(htype), range(10)):
                yield house
        else:
            for neighbourhood in self.neighbourhoods:
                for house in neighbourhood.houses[htype]:
                    yield house
    
    def has_store(self, htype, at_least=1):
        try:
            for neighbourhood in self.neighbourhoods:
                at_least += -1*neighbourhood.house_amounts[htype]
                if at_least <= 0:
                    return True
            else:
                return False
        except KeyError:
            return False

    def __has_class(self, class_name):
        for neighbourhood in self.get_neighbourhoods():
            if neighbourhood.amount_class(class_name) > 0:
                return True
        else:
            return False