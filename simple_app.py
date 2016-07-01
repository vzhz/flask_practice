from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route(/"<name>") #NOW if add whatever_name in url, will say "whatever_name waves at you!"
def index(name="Veronica"):
    return "{} is waving at you!".format{name}

app.run(debug=True), port=8000, host='0.0.0.0')

