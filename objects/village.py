import random
from objects.neighbourhood import Neighbourhood

class Village:
    def __init__(self, seed, size):
        self.seed = seed
        self.name = seed
        self.size = size

        SIZE_TO_RANGE = {
            'tiny':         (  1,   2),
            'small':        (  3,   7),
            'medium':       (  8,  19),
            'average':      ( 20,  44),
            'big':          ( 45,  74),
            'huge':         ( 75, 149),
            'humongous':    (150, 400)
        }

        random.seed(self.seed)
        self.neighbourhoods = random.randint(*SIZE_TO_RANGE[size])
    
    def get_neighbourhoods(self):
        return [Neighbourhood(f"{self.seed}-{i}" for i in range(self.neighbourhoods))]
    
    def available_classes(self):
        classes = [
            "commoner",
            "guard",
            "barbarian",
            "bard",
            "cleric",
            "druid",
            "fighter",
            "monk",
            "paladin",
            "ranger",
            "rogue",
            "sorcerer",
            "warlock",
            "wizard",
            "artificer"
        ]

        for cl in classes:
            if self.__has_class(cl):
                yield cl

    def iter_over_class(self, class_name, page_number=None):
        if self.count_class(class_name) <= 100:
            for neighbourhood in self.get_neighbourhoods():
                for house in neighbourhood.get_houses(f'class-{class_name}'):
                    pass

    def count_class(self, class_name):
        return sum([neighbourhood.amount_class(class_name) for neighbourhood in self.get_neighbourhoods()])

    def __has_class(self, class_name):
        for neighbourhood in self.get_neighbourhoods():
            if neighbourhood.amount_class(class_name) > 0:
                return True
        else:
            return False