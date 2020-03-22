import random

def get_menu(wealth):
    this_menu = {}

    for meal in MENU:
        food_dic = MENU[meal]

        if random.random() < food_dic['chanceOfBeingAvailable']:
            this_menu[meal] = food_dic['prices'][wealth]

    return this_menu


MENU = {
    "Mug of Dwarven Ale": {
        "chanceOfBeingAvailable": 0.45,
        "prices": {
            'Squalid': '3cp',
            'Poor': '3cp',
            'Modest': '4cp',
            'Comfortable': '4cp',
            'Wealthy': '6cp',
            'Aristocratic': '8cp'
        }
    },
    "Mug of King's Ale": {
        "chanceOfBeingAvailable": 0.75,
        "prices": {
            'Squalid': '3cp',
            'Poor': '3cp',
            'Modest': '4cp',
            'Comfortable': '4cp',
            'Wealthy': '6cp',
            'Aristocratic': '8cp'
        }
    },
    "Mug of Moon Mountain Ale": {
        "chanceOfBeingAvailable": 0.25,
        "prices": {
            'Squalid': '3cp',
            'Poor': '3cp',
            'Modest': '4cp',
            'Comfortable': '4cp',
            'Wealthy': '6cp',
            'Aristocratic': '8cp'
        }
    },
    "Mug of Spiced Ale": {
        "chanceOfBeingAvailable": 0.95,
        "prices": {
            'Squalid': '3cp',
            'Poor': '3cp',
            'Modest': '4cp',
            'Comfortable': '4cp',
            'Wealthy': '6cp',
            'Aristocratic': '8cp'
        }
    },
    "Mug of Trollbane Ale": {
        "chanceOfBeingAvailable": 0.7,
        "prices": {
            'Squalid': '3cp',
            'Poor': '3cp',
            'Modest': '4cp',
            'Comfortable': '4cp',
            'Wealthy': '6cp',
            'Aristocratic': '8cp'
        }
    },
    "Banquet (per person)": {
        "chanceOfBeingAvailable": 0.2,
        "prices": {
            'Squalid': '7gp',
            'Poor': '8gp',
            'Modest': '10gp',
            'Comfortable': '10gp',
            'Wealthy': '12gp',
            'Aristocratic': '25gp'
        }
    },
    "Bread, loaf": {
        "chanceOfBeingAvailable": 0.9,
        "prices": {
            'Squalid': '1cp',
            'Poor': '2cp',
            'Modest': '2cp',
            'Comfortable': '2cp',
            'Wealthy': '5cp',
            'Aristocratic': '1sp'
        }
    },
    "Cheese (hunk)": {
        "chanceOfBeingAvailable": 0.4,
        "prices": {
            'Squalid': '8cp',
            'Poor': '1sp',
            'Modest': '1sp',
            'Comfortable': '2sp',
            'Wealthy': '3sp',
            'Aristocratic': '5sp'
        }
    },
    "Various ferns, from fiddleheads to stewed broadleaves": {
        "chanceOfBeingAvailable": 0.3,
        "prices": {
            'Squalid': '2cp',
            'Poor': '3cp',
            'Modest': '4cp',
            'Comfortable': '5cp',
            'Wealthy': '8cp',
            'Aristocratic': '1sp'
        }
    },
    "Inn stay (per day)": {
        "chanceOfBeingAvailable": 1,
        "prices": {
            'Squalid': '7cp',
            'Poor': '1sp',
            'Modest': '5sp',
            'Comfortable': '8sp',
            'Wealthy': '2gp',
            'Aristocratic': '4gp'
        }
    },
    "Meals (per day)": {
        "chanceOfBeingAvailable": 1,
        "prices": {
            'Squalid': '3cp',
            'Poor': '6cp',
            'Modest': '3sp',
            'Comfortable': '5sp',
            'Wealthy': '8sp',
            'Aristocratic': '2gp'
        }
    },
    "Meat (chunk)": {
        "chanceOfBeingAvailable": 0.6,
        "prices": {
            'Squalid': '14cp',
            'Poor': '2sp',
            'Modest': '3sp',
            'Comfortable': '4sp',
            'Wealthy': '6sp',
            'Aristocratic': '1gp'
        }
    },
    "Common Wine (pitcher)": {
        "chanceOfBeingAvailable": 0.75,
        "prices": {
            'Squalid': '9cp',
            'Poor': '1sp',
            'Modest': '2sp',
            'Comfortable': '2sp',
            'Wealthy': '3sp',
            'Aristocratic': '5sp'
        }
    },
    "Fine Wine (bottle)": {
        "chanceOfBeingAvailable": 0.3,
        "prices": {
            'Squalid': '8gp',
            'Poor': '8gp',
            'Modest': '10gp',
            'Comfortable': '12gp',
            'Wealthy': '12gp',
            'Aristocratic': '20gp'
        }
    },
    "Messenger": {
        "chanceOfBeingAvailable": 0.1,
        "prices": {
            'Squalid': '2cp',
            'Poor': '4cp',
            'Modest': '6cp',
            'Comfortable': '1sp',
            'Wealthy': '1sp',
            'Aristocratic': '5sp'
        }
    },
    "Untrained Hireling (per day)": {
        "chanceOfBeingAvailable": 0.35,
        "prices": {
            'Squalid': '1sp',
            'Poor': '15cp',
            'Modest': '2sp',
            'Comfortable': '3sp',
            'Wealthy': '3sp',
            'Aristocratic': '5sp'
        }
    },
    "Skilled Hireling (per day)": {
        "chanceOfBeingAvailable": 0.1,
        "prices": {
            'Squalid': '1gp',
            'Poor': '15sp',
            'Modest': '2gp',
            'Comfortable': '3gp',
            'Wealthy': '3gp',
            'Aristocratic': '5gp'
        }
    }
}