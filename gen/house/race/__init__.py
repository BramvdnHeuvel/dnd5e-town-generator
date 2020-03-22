import random, json

with open('data/races.json', 'r') as open_file:
    __obj = json.load(open_file)
    
    RACE_BY_WEIGHT = {race: __obj[race]['density'] for race in __obj}
    TOTAL = sum(RACE_BY_WEIGHT.values())

def race(seed):
    random.seed(seed)
    r = random.randint(1, TOTAL)

    for race in RACE_BY_WEIGHT:
        r = r - RACE_BY_WEIGHT[race]
        if r <= 0:
            return race

