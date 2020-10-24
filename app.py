from flask import flask

app = Flask(__name__)

@app.route('/')
def firstApp():
    return "<h1> Minha primeira aplicação feita em flask </h1>"


if __name__ == "__main__":
    app.run()
