from flask import Flask, render_template, redirect, url_for
from objects import Village

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
    v = Village(town_name, size)

    if v.count_class(class_name) <= 50: # Should be <= 50 in production
        return render_template('all-of-class.html', 
                class_name=class_name,
                people=Village(town_name, size).iter_over_class(class_name),
                town=town_name,
                size=size
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
    v = Village(town_name, size)
    population = v.count_class(class_name)

    if population < 50:
        return redirect(url_for('show_people_of_class', town_name=town_name, size=size, class_name=class_name))
    
    elif population >= page*50:
        return render_template('some-of-class.html', 
                class_name=class_name,
                people=v.iter_over_class(class_name, page),
                town=town_name,
                size=size,
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

@app.route('/<town_name>/<size>/npc/<int:npc_number>')
def get_npc(town_name, size, npc_number):
    v = Village(town_name, size)
    return render_template('show-person.html',
        npc=v.find_npc(npc_number),
        town_name=town_name,
        size=size
    )

if __name__ == '__main__':
    app.run(debug=True)