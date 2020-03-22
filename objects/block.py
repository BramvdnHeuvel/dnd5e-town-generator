def cached_property(func):
    fname = func.__name__

    def exec(self):
        val = getattr(self, f'__{fname}', None)
        if val is not None:
            return val

        x = func(self)

        setattr(self, f'__{fname}', x)
        return x

    return property(exec)

NEIGHBOURHOOD_SIZE_TO_RANGE = {
    'tiny':         (  1,   2),
    'small':        (  5,   8),
    'medium':       ( 15,  20),
    'average':      ( 35,  45),
    'big':          ( 90, 140),
    'huge':         (250, 400),
    'humongous':    (800, 999),
    'massive':      (40000, 50000)
}

AVAILABLE_CLASS = [
    "commoner",
    "guard",
    "barbarian",
    "bard",
    "cleric",
    "druid",
    "fighter",
    "monk",
    "paladin",
    "ranger",
    "rogue",
    "sorcerer",
    "warlock",
    "wizard",
    "artificer"
]

HOUSES_PER_NEIGHBOURHOOD = {
    'blacksmith': {
            0: 0.05,
            1: 0.75,
            2: 0.10,
            3: 0.05,
            4: 0.05
        },
    'magic_shop': {
            0: 0.95,
            1: 0.05
        },
    'scrolls': {
            0: 0.45,
            1: 0.40,
            2: 0.10,
            3: 0.05
        },
    'jewelry': {
            0: 0.30,
            1: 0.40,
            2: 0.30
        },
    'general': {
            0: 0.05,
            1: 0.95
        },
    'tavern': {
            1: 1
        },
    'guard': {
            1: 0.05,
            2: 0.40,
            3: 0.35,
            4: 0.15,
            5: 0.05
        }
}

RACE_BY_WEIGHT = {
    'Human':              800000,
    'Half-elf':           100000,
    'Dwarf':               60000,
    'Elf':                 35000,
    'Half-orc':            25000,
    'Halfling':            20000,
    'Dragonborn':          10000,
    'Tiefling':            10000,
    'Gnome':               10000,
    'Aasimar':              9000,
    'Orc':                  8000,
    'Goliath':              7500,
    'Tabaxi':               5000,
    'Hobgoblin':            2500,
    'Lizardfolk':           1500,
    'Goblin':               1000,
    'Yuan-ti Pureblood':    1000,   
    'Bugbear':              1000,
    'Tortle':               1000,
    'Warforged':            1000,
    'Kobold':                800,
    'Shifter':               750,
    'Triton':                400,
    'Firbolg':               300,
    'Kalashtar':             250,
    'Aarakocra':             250,
    'Kenku':                 200,
    'Changeling':             50,
    'Gith':                   75,
    'Air Genasi':             10,
    'Earth Genasi':           10,
    'Fire Genasi':            10,
    'Water Genasi':           10,
}