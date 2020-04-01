import json

def accept_all_recipes():
    with open('data/menu.json', 'r') as menu_file:
        MENU = json.load(menu_file)

    with open('data/contributions/food.json') as open_file:
        for food in json.load(open_file):
            if food['food'] in MENU:
                print(f'{food["food"]} already exists on the menu.')
            else:
                MENU[food['food']] = {
                    'chanceOfBeingAvailable': food['rarity'],
                    'prices': food['prices']
                }
                add_contribution(food['author'])
    
    json.dump(MENU, open('data/menu.json', 'w'), indent=4)
            

def add_contribution(username):
    with open('data/contributions/contributors.json', 'r') as open_file:
        CONTS = json.load(open_file)
    
    if username == "Unknown":
        pass
    elif username in CONTS:
        CONTS[username] += 1
    else:
        CONTS[username] = 1
    
    json.dump(CONTS, open('data/contributions/contributors.json', 'w'), indent=4)