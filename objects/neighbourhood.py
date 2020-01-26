import random
from objects.house import House

class Neighbourhood:
    def __init__(self, seed):
        self.seed = seed
    
        random.seed(seed)
        self.blacksmiths = self.choose_from_dict('blacksmiths', {
            0: 0.05,
            1: 0.75,
            2: 0.10,
            3: 0.05,
            4: 0.05
        })
        self.magic_shops = self.choose_from_dict('magic_shop', {
            0: 0.95,
            1: 0.05
        })
        self.scrolls = self.choose_from_dict('scrolls', {
            0: 0.45,
            1: 0.40,
            2: 0.10,
            3: 0.05
        })
        self.jewelry = self.choose_from_dict('jewelry', {
            0: 0.30,
            1: 0.40,
            2: 0.30
        })
        self.general = self.choose_from_dict('general', {
            0: 0.05,
            1: 0.95
        })
        self.tavern = self.choose_from_dict('tavern', {
            1: 1
        })
        self.guards = self.choose_from_dict('guard', {
            1: 0.05,
            2: 0.40,
            3: 0.35,
            4: 0.15,
            5: 0.05
        })
        self.houses = random.randint(30, 60)

        self.AMOUNT_FOR_TYPE = {
            'blacksmith': self.blacksmiths,
            'magic_shop': self.magic_shops,
            'scrolls'   : self.scrolls,
            'jewelry'   : self.jewelry,
            'general'   : self.general,
            'tavern'    : self.tavern,
            'class-commoner'    : self.houses,
            'class-guard'       : self.guards,
            'class-barbarian'   : max(0, random.randint(0, 7)-5),
            'class-bard'        : random.randint(0, 3),
            'class-cleric'      : random.randint(0, 2),
            'class-druid'       : max(0, random.randint(0, 15)-13),
            'class-fighter'     : max(0, random.randint(0, 10)-9),
            'class-monk'        : max(0, random.randint(0, 11)-10),
            'class-paladin'     : max(0, random.randint(0, 16)-13),
            'class-ranger'      : max(0, random.randint(0, 15)-13),
            'class-rogue'       : max(0, random.randint(0, 25)-20),
            'class-sorcerer'    : max(0, random.randint(0, 10)-8),
            'class-warlock'     : max(0, random.randint(0, 18)-16),
            'class-wizard'      : max(0, random.randint(0, 8)-7),
            'class-artificer'   : max(0, random.randint(0, 27)-25)
        }

    def amount_class(self, class_name):
        if f'class-{class_name}' in self.AMOUNT_FOR_TYPE:
            return self.AMOUNT_FOR_TYPE[f'class-{class_name}']
        else:
            return 0

    def __get_houses_gen(self, specific_type):
        for i in range(self.AMOUNT_FOR_TYPE[specific_type]):
            yield House(f"{self.seed}-{specific_type}-{i}", specific_type)
    
    def get_houses(self, htype=None):
        if htype is not None:
            try:
                return [house for house in self.__get_houses_gen(htype)]
            except KeyError:
                raise IndexError("Specific house type does not exist.")
    
        houses = []
        
        for key in self.AMOUNT_FOR_TYPE:
            for house in self.__get_houses_gen(key):
                houses.append(house)
        
        return houses

    def choose_from_dict(self, name, dic):
        random.seed(f'{self.seed}-{name}')

        x = random.random()

        for key in dic:
            x = x - dic[key]
            if x < 0:
                return key