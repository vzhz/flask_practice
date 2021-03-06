from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
@app.route(/"<name>") #NOW if add whatever_name in url, will say "whatever_name waves at you!"
def index(name="Veronica"):
    return "{} is waving at you!".format{name}

#playing with types (when entered as strings, 2+5=25)
@app.route('/add/<int:num1>/<int:num2>')
@app.route('/add/<float:num1>/<float:num2>')
@app.route('/add/<int:num1>/<float:num2>')
@app.route('/add/<float:num1>/<int:num2>')
def add(num1, num2):
    context = {'num1' : num1, 'num2' : num2}
    return render_template('add.html', **context)

app.run(debug=True, port=8000, host='0.0.0.0')

