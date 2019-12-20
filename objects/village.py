import random
from objects.neighbourhood import Neighbourhood

class Village:
    def __init__(self, seed, size):
        self.seed = seed

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