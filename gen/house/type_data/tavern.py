import random, json

with open('data/menu.json', 'r') as open_file:
    MENU = json.load(open_file)
    RICHNESS = ['Squalid', 'Poor', 'Modest', 'Comfortable', 'Wealthy', 'Aristocratic']



def get_data():
    richness = random.choice(RICHNESS)
    menu = get_menu(richness)

    return {
        'menu': menu
    }

def get_menu(wealth):
    this_menu = {}

    for meal in MENU:
        food_dic = MENU[meal]

        if random.random() < food_dic['chanceOfBeingAvailable']:
            this_menu[meal] = food_dic['prices'][wealth]

    return this_menu
