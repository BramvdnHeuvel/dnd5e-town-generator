import json, random

with open('data/commoner-occupations.json', 'r') as open_file:
    OCCUPATIONS = json.load(open_file)

tot = 0
for occ in OCCUPATIONS:
    tot += 1 / OCCUPATIONS[occ]
    OCCUPATIONS[occ] = tot

def get_occupation(seed):
    random.seed(seed)

    r = random.random()

    for occ in OCCUPATIONS:
        if r < OCCUPATIONS[occ]:
            return occ
    else:
        return 'Commoner'