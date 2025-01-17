#!/usr/bin/python3
"""starts a Flask web application."""


from flask import Flask

app = Flask(__name__)


# defination with strict_slashes=False
@app.route('/', strict_slashes=False)
def hello_hbnb():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'


if __name__ == '__main__':
    # runc on 0.0.0.0:5000
    app.run(host='0.0.0.0', port=5000)
