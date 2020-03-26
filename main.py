from flask import Flask, render_template, redirect, url_for, request
from objects import Village, clean_tree, PASSWORD
from src.extractor import iter_over_people
from src.sanitizer import correct_size_only
from src.traffic import add_statistics

app = Flask(__name__)
app.route = add_statistics(app.route)

@app.route('/', methods=['GET', 'POST'])
def town_menu():
    clean_tree()
    if request.method == 'GET':
        return render_template('index.html')

    if 'town_name' in request.form and 'size' in request.form:
        return redirect(url_for('show_town', 
                                    town_name=request.form['town_name'], 
                                    size=request.form['size']
                                ))
    else:
        return render_template('index.html')

@app.route('/town/<town_name>/<size>')
@correct_size_only
def show_town(town_name, size):
    return render_template('town.html', town=Village(town_name, size))

@app.route('/<town_name>/<size>/store/<store_type>')
def show_all_stores(town_name, size, store_type):
    return render_template('all-of-store.html',
            town=Village(town_name, size),
            htype=store_type
        )

@app.route('/<town_name>/<size>/class/<class_name>')
def show_people_of_class(town_name, size, class_name):
    town = Village(town_name, size)
    try:
        population = town.classes[class_name]
    except KeyError:
        return redirect(url_for('show_town', town_name=town.name, size=town.size))

    if population['total'] <= 50:
        return render_template('all-of-class.html', 
                town=Village(town_name, size),
                class_name=class_name,
                people=iter_over_people(town, class_name)
        )
    else:
        return redirect(url_for('show_people_of_class_at_page',
                                    town_name=town_name,
                                    size=size,
                                    class_name=class_name,
                                    page=0
                                )
                        )

@app.route('/<town_name>/<size>/class/<class_name>/<int:page>')
def show_people_of_class_at_page(town_name, size, class_name, page):
    town = Village(town_name, size)
    try:
        population = town.classes[class_name]['total']
    except KeyError:
        return redirect(url_for('show_town', town_name=town.name, size=town.size))

    if population < 50:
        return redirect(url_for('show_people_of_class', town_name=town_name, size=size, class_name=class_name))
    
    elif population >= page*50:
        return render_template('some-of-class.html', 
                town=town,
                class_name=class_name,
                people=iter_over_people(town, class_name, page),
                page=page,
                last_page=(int(population/50) == page)
        )
    
    else:
        return redirect(url_for('show_people_of_class_at_page',
                                    town_name=town.name,
                                    size=town.size,
                                    class_name=class_name,
                                    page = population // 50
                                )
                        )

@app.route('/<town_name>/<size>/npc/<int:neighbourhood>/<class_name>/<int:house>/<int:person>')
def get_npc(town_name, size, neighbourhood, class_name, house, person):
    seed = (PASSWORD, town_name, size, neighbourhood, class_name, house, person)
    town = Village(town_name, size)
    person = town.find('person', seed)

    return render_template('show-person.html',
        town=town,
        person=person,
    )

@app.route('/<town_name>/<size>/house/<house_type>/<int:neighbourhood>/<int:house_id>')
def get_house(town_name, size, house_type, neighbourhood, house_id):
    if house_type == 'Barkeep':
        return redirect(url_for('get_tavern', 
                                    town_name=town_name,
                                    size=size,
                                    neighbourhood=neighbourhood,
                                    tavern_id=house_id
                                )
                        )
    
    seed = (PASSWORD, town_name, size, neighbourhood, house_type, house_id)

    town = Village(town_name, size)
    house = town.find('house', seed)

    if house is not None and house.extra_data != {}:
        return render_template('show-shop.html', town=town, shop=house)
    else:
        return redirect(url_for('show_town', town_name=town_name, size=size))

@app.route('/<town_name>/<size>/tavern/<int:neighbourhood>/<int:tavern_id>')
def get_tavern(town_name, size, neighbourhood, tavern_id):
    seed = (PASSWORD, town_name, size, neighbourhood, 'Barkeep', tavern_id)

    town = Village(town_name, size)
    tavern = town.find('house', seed)
    return render_template('show-tavern.html', tavern=tavern, town=town)

@app.route('/<town_name>/<size>/tavern-guests/<int:neighbourhood>/<int:tavern_id>/<int:time>')
def tavern_guests_at_given_time(town_name, size, neighbourhood, tavern_id, time):
    seed = (PASSWORD, town_name, size, neighbourhood, 'Barkeep', tavern_id)

    town = Village(town_name, size)
    tavern = town.find('house', seed)

    if tavern is None:
        return redirect(url_for('show_town', town_name=town.name, size=town.size))

    for guest_data in tavern.extra_data['guests']:
        if guest_data['time'] == time:
            return render_template('tavern-guests.html', town=town, tavern=tavern, g=guest_data)
    else:
        return 'The tavern is closed at this time.'

if __name__ == '__main__':
    app.run(debug=True)