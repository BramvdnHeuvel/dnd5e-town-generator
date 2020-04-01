from flask import url_for
import random, json


def get_data(tavern):
    RICHNESS = ['Squalid', 'Poor', 'Modest', 'Comfortable', 'Wealthy', 'Aristocratic']
    richness = random.choice(RICHNESS)
    menu = get_menu(richness)

    link = url_for('get_tavern', 
                            town_name=tavern.seed[1],
                            size=tavern.seed[2],
                            neighbourhood=tavern.seed[3],
                            tavern_id=tavern.seed[5]
                        )

    # The following functions depend on other seeds,
    # therefore HAVE to be used last.
    guest_list = guests(tavern)
    graph = build_graph(guest_list)

    return {
        'menu': menu,
        'guests': guest_list,
        'graph': graph,
        'link': f'<a href="{link}">{tavern.name}</a>'
    }

def build_graph(guest_list):
    dic = {'text': [], 'rect': []}

    g = [{'time': moment['time'], 'guests': len(moment['guests']) + len(moment['specialGuests'])} for moment in guest_list]
    maximum_height = max([moment['guests'] for moment in g])

    for moment, i in zip(g, range(24)):
        dic['text'].append({
            'x': 37*i,
            'y': maximum_height + 20,
            'value': str(moment['time']) 
        })
        dic['rect'].append({
            'x': 37*i + 1,
            'y': maximum_height-moment['guests'],
            'width': 35,
            'height': moment['guests'],
            'time': moment['time']
        })
    else:
        i += 1
        dic['text'].append({
            'x': 37*i,
            'y': maximum_height + 20,
            'value': str(moment['time']+1)
        })
    return dic

def guests(tavern):
    neighbourhood = tavern.neighbourhood
    start = 10 if tavern.family_schedule[10][1] == 2 else 11

    guest_list = [{'time': i%24, 'guests': [], 'specialGuests': []} for i in range(start, start+17)]

    for moment in guest_list:
        for occup in neighbourhood.houses:
            for house in neighbourhood.houses[occup]:
                activity = house.family_schedule[moment['time']][1]
                if activity > 2:
                    for person in house.inhabitants:
                        if activity == 3 or person.is_mature:
                            p_type = 'guests' if person.class_name in ['Commoner', 'Guard'] else 'specialGuests'
                            moment[p_type].append(person)

    return guest_list 

def get_menu(wealth):
    with open('data/menu.json', 'r') as open_file:
        MENU = json.load(open_file)

    this_menu = {}

    for meal in MENU:
        food_dic = MENU[meal]

        if random.random() < food_dic['chanceOfBeingAvailable']:
            this_menu[meal] = food_dic['prices'][wealth]

    return this_menu
