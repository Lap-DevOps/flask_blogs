from flask import Flask, render_template, url_for, request, flash, session, redirect, abort

app = Flask(__name__)

# Установка секретного ключа
app.secret_key = 'your_secret_key_here'

menu = [{'name': "Setup", "url": 'install-flask'},
        {'name': "First App", "url": 'first-app'},
        {'name': "Contact", "url": 'contact'},
        ]


@app.route('/')
def index():
    print(url_for('index'))
    return render_template("index.html", menu=menu)


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
