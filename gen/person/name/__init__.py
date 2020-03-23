from gen.person.name import (
    aarakocra,
    dragonborn,
    dwarf,
    elf,
    halfelf,
    halfling,
    halforc,
    human,
    tiefling
)
import random

RACE_BY_MODULE = {
    'aarakocra'     :   aarakocra,
    'dragonborn'    :   dragonborn,
    'dwarf'         :   dwarf,
    'elf'           :   elf,
    'half-elf'      :   halfelf,
    'halfling'      :   halfling,
    'half-orc'      :   halforc,
    'human'         :   human,
    'tiefling'      :   tiefling
}

def last_name(seed, race):
    random.seed(str(seed))
    return get_name_from_race(race, 'last_name')

def first_name(seed, race, gender):
    random.seed(str(seed))
    return get_name_from_race(race, gender.lower())

def get_name_from_race(race, name_type):
    name_type = name_type.lower()
    try:
        module = RACE_BY_MODULE[race.lower()]
    except KeyError:
        return 'Ya boi nameless'
    else:
        if name_type == 'male':
            return module.male()
        if name_type == 'female':
            return module.female()
        if name_type == 'last_name':
            return module.last_name()
        if name_type == 'male_full':
            return module.male() + ' ' + module.last_name()
        if name_type == 'female_full':
            return module.female() + ' ' + module.last_name()
        return None

def get_race_list():
    return [race for race in RACE_BY_MODULE]