from gen.person.name import (
    aarakocra,
    aasimar,
    bugbear,
    changeling,
    dragonborn,
    dwarf,
    elf,
    genasi,
    gith,
    gnome,
    goblin,
    goliath,
    halfelf,
    halfling,
    halforc,
    hobgoblin,
    human,
    kalashtar,
    kenku,
    kobold,
    lizardfolk,
    orc,
    shifter,
    tabaxi,
    tiefling,
    tortle,
    triton,
    warforged,
    yuan_ti
)
import random

RACE_BY_MODULE = {
    'aarakocra'         :   aarakocra,
    'aasimar'           :   aasimar,
    'air genasi'        :   genasi.air,
    'bugbear'           :   bugbear,
    'changeling'        :   changeling,
    'dragonborn'        :   dragonborn,
    'dwarf'             :   dwarf,
    'earth genasi'      :   genasi.earth,
    'elf'               :   elf,
    'firbolg'           :   elf,            # Use the same names as elves
    'fire genasi'       :   genasi.fire,
    'gith'              :   gith,
    'gnome'             :   gnome,
    'goblin'            :   goblin,
    'goliath'           :   goliath,
    'half-elf'          :   halfelf,
    'halfling'          :   halfling,
    'half-orc'          :   halforc,
    'hobgoblin'         :   hobgoblin,
    'human'             :   human,
    'kalashtar'         :   kalashtar,
    'kobold'            :   kobold,
    'kenku'             :   kenku,
    'lizardfolk'        :   lizardfolk,
    'orc'               :   orc,
    'shifter'           :   shifter,
    'tiefling'          :   tiefling,
    'tabaxi'            :   tabaxi,
    'tortle'            :   tortle,
    'triton'            :   triton,
    'warforged'         :   warforged,
    'water genasi'      :   genasi.water,
    'yuan-ti pureblood' :   yuan_ti
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