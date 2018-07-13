from flask import Flask

app = Flask(__name__)
#app.config['DEBUG']=True

@app.route("/<string:name>")

def hello(name):
    name = name.capitalize()
    return f"Hello, {name}!"
