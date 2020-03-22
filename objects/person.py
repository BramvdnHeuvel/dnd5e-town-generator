from gen.name import get_name_from_race
from gen.misc.inventory import get_inventory
from objects.block import cached_property
import random

class Person:
    def __init__(self, seed, race, gender, age, clss='commoner', name='', is_mature=True, number=0):
        self.seed = seed
        self.gender = gender
        self.race = race
        self.class_name = clss
        self.age = age
        self.last_name = name
        self.is_mature = is_mature
        self.number = number

    @cached_property
    def schedule(self):
        num_dic = {
            0: 'Asleep',
            1: 'Doing nothing in particular',
            2: 'Hanging out in the tavern',
            3: 'Eating food at the tavern'
        }
        if self.class_name != 'commoner':
            num_dic[2] = 'At work'
        if not self.is_mature:
            num_dic[2] = 'Playing outside'

        random.seed(f'{self.seed}-schedule')
        return [num_dic[i] for i in self.__build_schedule()]
    
    @cached_property
    def inventory(self):
        random.seed(f'{self.seed}-inventory')
        return get_inventory

    @cached_property
    def level(self):
        if self.class_name == 'commoner':
            return 1

        random.seed(f'{self.seed}-level')

        level = 1
        while random.random() < 0.7 and level < 20:
            level += 1
        return level

    @cached_property
    def name(self):
        random.seed(f'{self.seed}-name')
        return get_name_from_race(self.race, self.gender) + self.last_name

    def __build_schedule(self):
        if self.class_name == 'class-commoner':
            wake_up = random.randint(4, 12)
            lunch = random.randint(11, 15)
            dinner = lunch + 6
            drunk = random.randint(16, 21)

            for i in range(24):
                if i + 24 > wake_up + 16 and i < wake_up:
                    yield 0 # Asleep
                elif i in [lunch, dinner]:
                    yield 3 # Eating food at the tavern
                elif i in [drunk, drunk + 1, drunk + 2]:
                    yield 2 # Drinking at the tavern
                else:
                    yield 1 # Doing nothing in particular
                
        else:
            wake_up = random.randint(5, 8)
            work = random.randint(8, 10)
            lunch = random.randint(11, 14)
            dinner = work + 9

            for i in range(24):
                if i < wake_up or i >= (wake_up + 16):
                    yield 0  # Asleep
                elif i in [lunch, dinner]:
                    yield 3 # Eating food at the taven
                elif i >= work and i < dinner:
                    yield 2 # At work
                else:
                    yield 1 # Doing nothing in particular 

