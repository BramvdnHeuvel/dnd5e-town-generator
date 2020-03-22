from flask import Flask

app = Flask(__name__)

@app.route('/hello')
def say_hello():
    return '<p style="color: red">Hello</p>'

app.run()