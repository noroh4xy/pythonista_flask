from app import pythonista, db
from flask import render_template, redirect, url_for, request, flash
from application.models import Users
from flask_login import login_user, current_user, logout_user, login_required


@pythonista.route("/", methods=['GET'])
def index():
    return render_template("index.html")


@pythonista.route("/signup", methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    if request.method == "POST":
        username = request.form['username']
        email = request.form['email']
        password1 = request.form['password1']
        password2 = request.form['password2']
        print(username, email, password2, password1)
        user = Users.query.filter_by(username=username).first()
        email = Users.query.filter_by(email=email).first()
        if user is not None or email is not None:
            flash("Username or Email is in use.")
            return redirect(url_for('signup'))
        if password1 == password2:
            new_user = Users(username=username, email=email, password=password2)
            db.session.add(new_user)
            db.session.commit()
            flash("You have been registered.")
            return redirect(url_for('login'))

        else:
            flash("Something went wrong, please try again!")
            return redirect(url_for('signup'))

    return render_template("signup.html")


@pythonista.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']
        user = Users.query.filter_by(email=email).first()
        if user is not None and password == user.password:
            login_user(user=email)
        else:
            flash("Something went wrong, please try again!")
            return redirect(url_for('login'))

    return render_template("login.html")


@pythonista.route("/add-post", methods=['GET', 'POST'])
@login_required
def add_post():
    return render_template('post.html')


@pythonista.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("index"))
