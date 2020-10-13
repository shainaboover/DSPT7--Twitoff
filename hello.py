
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/new_page')
def new_page():
    return 'This is another page!'


# to run: export FLASK_APP.py (might be 'set' on some terminals)
# flask run

if __name__ == '__main__':
    app.run(debug=True)