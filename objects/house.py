import random
from objects.person import Person

class House:
    def __init__(self, seed, htype):
        self.seed = seed
        self.type = htype

        random.seed(seed)

        self.race = self.__extract_race_from_seed()
        self.inhabitants = self.__get_inhabitant_amount()

        self.genders = self.__get_random_genders()
    
    def get_inhabitants(self):
        return [p for p in self.__get_inhabitants_gen()]
    
    def __get_random_genders(self):
        if random.random() > 0.1:
            # Straight couple
            if random.random() < 0.5:
                gen = ['Male', 'Female']
            gen = ['Female', 'Male']
        else:
            # Gay couple
            if random.random() < 0.5:
                gen = ['Male', 'Male']
            gen = ['Female', 'Female']
        
        for _ in range(len(self.inhabitants)-2):
            if random.random() < 0.5:
                gen.append('Male')
            else:
                gen.append('Female')
        return gen

    def __extract_race_from_seed(self):
        pass    #! TODO
        return 'human'
    
    def __get_inhabitant_amount(self):
        return 0

    def __get_inhabitants_gen(self):
        for i, gender in zip(range(self.inhabitants), self.genders):
            yield Person(f'{self.seed}-p-{i}', self.race, gender, age='mature')
        
        for i in range(2, self.inhabitants):
            yield Person(f'{self.seed}-p-{i}', self.race, gender[i], age='child')