import random
from config import PREMIUM

NEIGHBOURHOOD_SIZE_TO_RANGE = {
    'tiny':         (  1,   2),
    'small':        (  5,   8),
    'medium':       ( 15,  20),
    'average':      ( 35,  45),
    'big':          ( 90, 140),
    'huge':         (250, 470)
}

if PREMIUM == True:
    NEIGHBOURHOOD_SIZE_TO_RANGE['humongous'] =  (800, 999)
    NEIGHBOURHOOD_SIZE_TO_RANGE['massive']   =  (4000, 5000)
    NEIGHBOURHOOD_SIZE_TO_RANGE['colossal']  =  (16000, 20000)


def get_neighbourhood_amount(seed, size):
    random.seed(str(seed))
    sizes = NEIGHBOURHOOD_SIZE_TO_RANGE[size]
    return random.randint(*sizes)
