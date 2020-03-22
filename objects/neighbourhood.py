import random
from objects.house import House
from objects.block import cached_property, HOUSES_PER_NEIGHBOURHOOD

class Neighbourhood:
    def __init__(self, seed, cursor):
        self.seed = seed
        self.cursor = cursor
    
    def __repr__(self):
        return f"<Neighbourhood {self.seed}>"

    @cached_property
    def house_amounts(self):
        random.seed(f'{self.seed}-amounts')

        return {
            'blacksmith': self.choose_from_dict('blacksmith'),
            'magic_shop': self.choose_from_dict('magic_shop'),
            'scrolls'   : self.choose_from_dict('scrolls'),
            'jewelry'   : self.choose_from_dict('jewelry'),
            'general'   : self.choose_from_dict('general'),
            'tavern'    : self.choose_from_dict('tavern'),
            'class-commoner'    : random.randint(30, 60),
            'class-guard'       : self.choose_from_dict('guard'),
            'class-barbarian'   : max(0, random.randint(0, 7)-5),
            'class-bard'        : random.randint(0, 3),
            'class-cleric'      : random.randint(0, 2),
            'class-druid'       : max(0, random.randint(0, 20)-19),
            'class-fighter'     : max(0, random.randint(0, 10)-9),
            'class-monk'        : max(0, random.randint(0, 11)-10),
            'class-paladin'     : max(0, random.randint(0, 16)-13),
            'class-ranger'      : max(0, random.randint(0, 15)-13),
            'class-rogue'       : max(0, random.randint(0, 25)-20),
            'class-sorcerer'    : max(0, random.randint(0, 10)-8),
            'class-warlock'     : max(0, random.randint(0, 18)-16),
            'class-wizard'      : max(0, random.randint(0, 9)-7),
            'class-artificer'   : max(0, random.randint(0, 27)-25)
        }

    @cached_property
    def houses(self):
        total = self.cursor
        dic = {}

        for htype in self.house_amounts:
            dic[htype] = []
            for i in range(self.house_amounts[htype]):
                house = House(f"{self.seed}-{htype}-{i}", htype, total)
                dic[htype].append(house)
                total += house.inhabitant_amount
        return dic

    @cached_property
    def inhabitants(self):
        return sum(self.house_amounts.values())

    def find_npc(self, number):
        if number < self.cursor or number >= self.cursor + self.inhabitants:
            return None
        total = self.cursor
        for htype in self.houses:
            for house in self.houses[htype]:
                if total + house.inhabitant_amount > number:
                    return house.inhabitants[number-total]
                total += house.inhabitant_amount
        else:
            raise ValueError("For some reason, the NPC was expected to be found in this neighbourhood!") 

    @staticmethod
    def choose_from_dict(name):
        dic = HOUSES_PER_NEIGHBOURHOOD[name]
        x = random.random()

        for key in dic:
            x = x - dic[key]
            if x < 0:
                return key