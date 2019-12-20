import random

class Person:
    def __init__(self, seed, race, gender, age='mature'):
        self.seed = seed
        self.gender = gender

        random.seed(seed)
        self.age = self.__get_age_by_race()
        self.schedule = self.__get_schedule()
        self.inventory = self.__get_inventory()
    
    def __get_age_by_race(self):
        return 50
    
    def __get_schedule(self):
        return [
            0, 0, 0, 0, 0, 0,   # 0 - sleep
            0, 1, 1, 2, 2, 2,   # 1 - nothing in particular
            2, 3, 2, 2, 2, 2,   # 2 - at work
            3, 1, 1, 1, 1, 0    # 3 - eating food at the tavern
        ]
    
    def __get_inventory(self):
        return []