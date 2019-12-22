"""Movie Ratings."""

from jinja2 import StrictUndefined

from flask import (Flask, render_template, redirect, request, flash, session)
from flask_debugtoolbar import DebugToolbarExtension

from model import User, Rating, Movie, connect_to_db, db


app = Flask(__name__)

# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"

# Normally, if you use an undefined variable in Jinja2, it fails
# silently. This is horrible. Fix this so that, instead, it raises an
# error.
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def index():
    """Homepage."""
    return render_template("homepage.html")

@app.route('/register')
def registration_form():
    """Shows the registration form for new users"""

    return render_template("registration_form.html")

@app.route('/register', methods=['POST'])
def register_confirmation():

    email = request.form.get("email")
    password = request.form.get("password")
    age = request.form.get("age")
    zipcode = request.form.get("zipcode")

    if User.query.filter(User.email == email).all():
        flash("Email already in use.")
        return redirect('/register')
    else:
        new_user = User(email=email, password=password, age=age, zipcode=zipcode)
        db.session.add(new_user)
        db.session.commit()

    return redirect('/')

@app.route('/login')
def login_form():

    return render_template("login_form.html")

@app.route('/login', methods=['POST'])
def login():

    email = request.form.get("email")
    password = request.form.get("password")
    login_query = User.query.filter(User.password == password, User.email == email).all()

    if login_query:
        session['current_user'] = login_query[0].user_id
        flash("Logged In")
        return redirect('/')
    else:
        flash("Information Incorrect")
        return redirect('/login')

@app.route('/logout')
def logout():
    """Logout"""

    session.clear()
    flash("Logged Out")

    return redirect('/')


@app.route("/users")
def user_list():
    """show list of users"""

    users = User.query.all()
    return render_template("user_list.html", users=users)


if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True
    # make sure templates, etc. are not cached in debug mode
    app.jinja_env.auto_reload = app.debug

    connect_to_db(app)

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(port=5000, host='0.0.0.0')
