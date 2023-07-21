import os
import sqlite3

from flask import Flask, render_template, url_for, request, flash, session, redirect, abort, g

from FDataBase import FDataBase

# config
DATABASE = 'tmp/flsite.db'
DEBUG = True
SECRET_KEY = 'sdlkslksdlklksdfklekllsd'

app = Flask(__name__)
app.config.from_object(__name__)
app.secret_key = SECRET_KEY
app.config.update(dict(DATABASE=os.path.join(app.root_path, 'flsite.db')))


def connect_db():
    conn = sqlite3.connect(app.config['DATABASE'])
    conn.row_factory = sqlite3.Row
    return conn


def create_db():
    db = connect_db()
    with app.open_resource("sq_db.sql", mode='r') as f:
        db.cursor().executescript(f.read())
        db.commit()
        db.close()


def get_db():
    if not hasattr(g, 'link_db'):
        g.link_db = connect_db()
    return g.link_db


@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'link_db'):
        g.link_db.close()


menu = [{'name': "Setup", "url": 'install-flask'},
        {'name': "First App", "url": 'first-app'},
        {'name': "Contact", "url": 'contact'},
        ]


@app.route('/')
def index():
    print(url_for('index'))
    db = get_db()
    dbase = FDataBase(db)
    # print (dbase.getMenu())
    return render_template("index.html", menu=dbase.getMenu(), posts=dbase.getPostsAnonce())


@app.route('/add_post', methods=['POST', "GET"])
def addPost():
    db = get_db()
    dbase = FDataBase(db)

    if request.method == "POST":
        if len(request.form['name']) > 4 and len(request.form['post']) > 10:
            res = dbase.addPost(request.form['name'], request.form['post'], request.form['url'])
            if not res:
                flash("Error adding post", category='error')
            else:
                flash("Post added", category='success')
        else:
            flash("Error adding post", category='error')
    return render_template('add_post.html', menu=dbase.getMenu(), title="Adding post")


@app.route('/post/<alias>')
def showPost(alias):
    db = get_db()
    dbase = FDataBase(db)
    title, post = dbase.getPost(alias)
    if not title:
        abort(404)

    return render_template('post.html', menu=dbase.getMenu(), title=title, post=post)


@app.route('/about')
def about():
    print(url_for('about'))
    return render_template("about.html", title="About", menu=menu)


@app.route("/contact", methods=["POST", "GET"])
def contact():
    if request.method == "POST":
        print(request.form)

        if len(request.form['username']) > 2:
            flash("Message send !", category='success')
        else:
            flash("Error !", category='error')

        for key, value in request.form.items():
            print(f"Key: {key} -  Value: {value}")
    return render_template("contact.html", title="Feedback", menu=menu)


@app.errorhandler(404)
def pageNotFound(error):
    return render_template("page404.html", title="Page not found", menu=menu), 404


@app.route('/profile/<username>')
def profile(username):
    if "userLogged" not in session or session['userLogged'] != username:
        abort(401)
    return f"Profile of user - {username}"


@app.route('/login', methods=["POST", "GET"])
def login():
    if 'userLogged' in session:
        return redirect(url_for('profile', username=session['userLogged']))
    elif request.method == "POST" and request.form['username'] == 'Mike' and request.form['psw'] == '123':
        session['userLogged'] = request.form['username']
        return redirect(url_for('profile', username=session['userLogged']))

    return render_template('login.html', title="Login page", menu=menu)


if __name__ == '__main__':
    app.run(debug=True)
