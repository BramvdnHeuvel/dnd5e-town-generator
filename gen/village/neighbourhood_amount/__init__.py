import random

NEIGHBOURHOOD_SIZE_TO_RANGE = {
    'tiny':         (  1,   2),
    'small':        (  5,   8),
    'medium':       ( 15,  20),
    'average':      ( 35,  45),
    'big':          ( 90, 140),
    'huge':         (250, 470),
    'humongous':    (800, 999),
    'massive':      (4000, 5000),
    'colossal':     (16000, 20000)
}

def get_neighbourhood_amount(seed, size):
    random.seed(str(seed))
    sizes = NEIGHBOURHOOD_SIZE_TO_RANGE[size]
    return random.randint(*sizes)
