from flask import Flask, render_template
from objects import Village

app = Flask(__name__)

@app.route('/town/<town_name>/<size>')
def show_town(town_name, size):
    return render_template('town.html', town=Village(town_name, size))

if __name__ == '__main__':
    app.run(debug=True)