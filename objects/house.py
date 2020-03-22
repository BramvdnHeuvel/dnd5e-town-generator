import random, math
from objects.person import Person
from gen.name.house_name import get as get_name
from gen.name import get_name_from_race as get_last_name
from gen.age import get_family_ages
from objects.block import cached_property, RACE_BY_WEIGHT

TOTAL = sum(RACE_BY_WEIGHT.values())

class House:
    def __init__(self, seed, htype, cursor):
        self.seed = seed
        self.type = htype
        self.cursor = cursor
    
    @cached_property
    def class_name(self):
        random.seed(f'{self.seed}-class_name')
        if self.type.startswith('class-'):
            return self.type.split('-')[-1]
        return 'commoner'

    @cached_property
    def store(self):
        if self.class_name != 'commoner':
            return {
                'name': 'Not a store',
                'owner': 'Not a store'
            }
        else:
            inhabitants = self.inhabitants
            random.seed(f'{self.seed}-store')
            return {
                'name': get_name(),
                'owner': inhabitants[0]
            }

    @cached_property
    def race(self):
        random.seed(f'{self.seed}-race')
        r = random.randint(1, TOTAL)

        for race in RACE_BY_WEIGHT:
            r = r - RACE_BY_WEIGHT[race]
            if r <= 0:
                return race

    @cached_property
    def inhabitant_amount(self):
        race = self.race
        random.seed(f'{self.seed}-inhabitant_amount')

        if self.type.startswith('class-') and self.type != 'class-commoner':
            return 1
            # DANGEROUS! We always assume that non-commoners aren't settled down and don't have a family.
            # Do not alter this number unless you know what you're doing.
        else:
            amount_of_race = RACE_BY_WEIGHT[race]
            if random.random() < math.sqrt(amount_of_race / TOTAL):
                return 2 + self.__extra_child()
            else:
                return 1 # Forever alone :(
    
    @cached_property
    def inhabitants(self):
        return [p for p in self.__inhabitants_gen()]

    @cached_property
    def ages(self):
        race = self.race
        amount = self.inhabitant_amount

        random.seed(f'{self.seed}-ages')
        return [age for age in get_family_ages(amount, race)]

    @cached_property
    def genders(self):
        amount = self.inhabitant_amount

        random.seed(f'{self.seed}-genders')
        if random.random() > 0.1:
            # Straight couple
            if random.random() < 0.5:
                gen = ['Male', 'Female']
            else:
                gen = ['Female', 'Male']
        else:
            # Gay couple
            if random.random() < 0.5:
                gen = ['Male', 'Male']
            gen = ['Female', 'Female']
        
        for _ in range(amount-2):
            if random.random() < 0.5:
                gen.append('Male')
            else:
                gen.append('Female')

        return gen
    
    @cached_property
    def last_name(self):
        race = self.race

        random.seed(f'{self.seed}-last-name')
        return ' ' + get_last_name(race, 'last_name')
    
    def __extra_child(self):
        if random.random() < 0.4:
            return 0
        else:
            return self.__extra_child() + 1

    def __inhabitants_gen(self):
        for i, gender, age in zip(range(self.inhabitant_amount), self.genders, self.ages):
            if i < 2:
                yield Person(
                    f'{self.seed}-person-{i}', 
                    self.race, 
                    gender, 
                    age=age, 
                    clss=self.class_name, 
                    name=self.last_name, 
                    is_mature=True,
                    number=self.cursor+i
                )
            else:
                yield Person(
                    f'{self.seed}-person-{i}', 
                    self.race, 
                    gender, 
                    age=age, 
                    clss='commoner', 
                    name=self.last_name, 
                    is_mature=False,
                    number=self.cursor+i
                )
