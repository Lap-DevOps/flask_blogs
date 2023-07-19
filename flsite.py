from flask import Flask, render_template, url_for, request, flash

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


@app.route("/profile/<path:username>/<path>")
def profile(username, path):
    return f'User : {username}, {path}'


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


if __name__ == '__main__':
    app.run(debug=True)
