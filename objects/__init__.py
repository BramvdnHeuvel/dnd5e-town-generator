from namegen import get_race_list
from objects.village import Village

def seed_builder(city_name, size, race_weights):
    seed = 'f{city_name}|{size}|'
    for race in get_race_list():
        if race in race_weights:
            seed += f'{race}:{int(race_weights[race])},'
        
        #! Do NOT add races that aren't part of the population!
        #! Doing so will make sure that every town gets reset whenever a new race is available.
    seed += '|'

    return seed

def unpack_seed(seed, expected_type):
    args = seed.split('-')

    EXPECTED_AMOUNT = {
        'village'   : 1,
        'house'     : 4,
        'person'    : 6
    }

    if expected_type not in EXPECTED_AMOUNT:
        raise ValueError(f"Unknown type '{expected_type}'")

    if len(args) != EXPECTED_AMOUNT[expected_type]:
        raise ValueError("Invalid seed type.")

    # -------------------------------------->

    if expected_type == 'village':
        village = Village(args[0])

    if expected_type == 'house':
        village = Village(args[0])
        try:
            neighbourhood = village.get_neighbourhoods()[int(args[1])]
        except IndexError:
            raise NameError("That neighbourhood does not exist.")
        
        try:
            house = neighbourhood.get_houses(args[2])[int(args[3])]
        except IndexError:
            raise NameError("That house does not exist.")
        except ValueError:
            raise ValueError("Invalid seed type.")
    
    if expected_type == 'person':
        village = Village(args[0])
        try:
            neighbourhood = village.get_neighbourhoods()[int(args[1])]
        except IndexError:
            raise NameError("That neighbourhood does not exist.")
        
        try:
            house = neighbourhood.get_houses(args[2])[int(args[3])]
        except IndexError:
            raise NameError("That house does not exist.")
        except ValueError:
            raise ValueError("Invalid seed type.")

        try:
            person = house.get_inhabitants()[int(args[5])]
        except IndexError:
            raise NameError("That person does not exist.")
