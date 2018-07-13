from flask import Flask

app = Flask(__name__)
#app.config['DEBUG']=True

@app.route("/<string:name>")

def index(name):
    name = name.Capitalize()
    return f"Hello, {name}!"
