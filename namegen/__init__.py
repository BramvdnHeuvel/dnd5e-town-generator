from namegen import (
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

def get_name_from_race(race, name_type):
    module = RACE_BY_MODULE[race]

    if name_type == 'male':
        return module.male()
    if name_type == 'female':
        return module.female()
    if name_type == 'last_name':
        return module.last_name()
    return None

def get_race_list():
    return [race for race in RACE_BY_MODULE]