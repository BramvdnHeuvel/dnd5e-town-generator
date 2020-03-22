import json, random

with open('data/occupations.json', 'r') as open_file:
    OCCUPATIONS = json.load(open_file)

def house_amounts(seed):
    random.seed(seed)
    dic = {}

    for occup in OCCUPATIONS:
        d = OCCUPATIONS[occup]
        dic[occup] = get_random_amount(d["n"], d["e"])
    
    # The odds are near impossible that the WHOLE neighbourhood is empty,
    # but let's just make sure that never happens.
    dic["Commoner"] = max(1, dic["Commoner"])
    # Yes, this means there will always be at least one commoner in every neighbourhood.

    return dic


def get_random_amount(n, e):
    p = e / n
    i = 0

    for _ in range(n):
        if random.random() < p:
            i += 1
    
    return i
