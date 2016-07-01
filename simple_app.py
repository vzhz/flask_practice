from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def index(name="Veronica", name): #if add ?name=whatever_name in url, will say "whatever_name waves at you!"
    return "{} is waving at you!".format{name}

app.run(debug=True), port=8000, host='0.0.0.0')

