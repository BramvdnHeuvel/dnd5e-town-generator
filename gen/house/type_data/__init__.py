import random
from gen.house.type_data import (
    tavern
)

DATA_MODULE = {
    'Tavern': tavern
}

def get_house_type_data(seed, house_type):
    random.seed(seed)
    return DATA_MODULE[house_type].get_data()