from flask import *

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")


@app.route('/signup')
def signup():
    return render_template("signup.html")


if __name__ == '__main__':
    app.run()
