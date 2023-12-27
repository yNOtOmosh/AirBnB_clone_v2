from flask import Flask

app = Flask(__name__)

# defination with strict_slashes=False
@app.route('/', strict_slashes=False)
def hello_hbnb():
    return 'Hello HBNB!'

if __name__ == '__main__':
    # run on 0.0.0.0:5000
    app.run(host='0.0.0.0', port=5000)
