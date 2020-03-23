from flask import Flask, render_template, redirect, url_for
from objects import Village, clean_tree, PASSWORD
from src.extractor import iter_over_people

app = Flask(__name__)

@app.route('/town/<town_name>/<size>')
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

    if town.classes[class_name]['total'] <= 50:
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
    population = town.classes[class_name]['total']

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
                                    town_name=town_name,
                                    size=size,
                                    class_name=class_name,
                                    page=population // 50
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

if __name__ == '__main__':
    app.run(debug=True)