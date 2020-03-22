import random, json

with open('occupations.json', 'r') as open_file:
    FAMILY = json.load(open_file)
    FAMILY = {job: FAMILY[job]['family'] for job in FAMILY}

with open('data/race.json', 'r') as open_file:
    RACES = json.load(open_file)
    RACES = {race: RACES['density'] for race in RACES}
    TOTAL = sum(RACES.value())


def get_inhabitants(seed, house_type, race):
    random.seed(seed)

    if FAMILY[house_type] == False:
        return 1

    density = RACES[race]
    if random.random() < 0.5*(1 - (TOTAL-density/TOTAL)**150):
        # Provided that there are enough of the same kind to
        # fall in love with, every member of the society has
        # a 50-50 chance to be in a relationship.
        # This means that about 2/3 of humans have a relationship,
        # while a Genasi will probably never find another Genasi
        # and hence not fall in love.
        # (
        #  And I don't know which races can or can't fall in love
        #  with each other, so we're keeping races divided from
        #  each other.
        # )

        return 2 + extra_child()
    else:
        # The person does not live together with anyone at the moment.
        return 1

def extra_child():
    if random.random() < 0.6:
        return 0
    else:
        return 1 + extra_child()