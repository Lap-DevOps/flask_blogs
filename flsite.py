from flask import Flask

app = Flask(__name__)

@app.route('/index')
@app.route('/')
def index():
    return '<h1>index </h1>'


@app.route('/about')
def about():
    return "<h2>About</h2>"


if __name__ == '__main__':
    app.run(debug=True)
