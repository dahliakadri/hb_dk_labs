"""A madlib game that compliments its users."""

from random import choice

from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful',
    'smashing', 'lovely',
]


@app.route('/')
def start_here():
    """Display homepage."""

    return "Hi! This is the home page."


@app.route('/hello')
def say_hello():
    """Say hello to user."""

    return render_template("hello.html")


@app.route('/greet')
def greet_person():
    """Greet user with compliment."""

    player = request.args.get("person")

    compliment = choice(AWESOMENESS)

    return render_template("compliment.html",
                           person=player,
                           compliment=compliment)


@app.route('/game')
def show_madlib_form():
    """Get user response to play a game"""
    response = request.args.get("yesno")

    if response == "no":
        return render_template("goodbye.html")
    else:
        return render_template("game.html")


@app.route('/madlib')
def show_madlib():
    """Create a madlib based on user input from game."""
    madlib_temp_list = ["madlib.html", "madlib2.html", "madlib3.html"]
    person = request.args.get("person")
    color = request.args.get("color")
    noun = request.args.get("noun")   
    adjective = request.args.get("adjective")
    adjective2 = request.args.get("adjective2", '')
    adjective3 = request.args.get("adjective3", '')
    adjective4 = request.args.get("adjective4", '')

    return render_template(choice(madlib_temp_list),
                           person=person,
                           color=color,
                           noun=noun,
                           adjective=adjective,
                           adjective2=adjective2,
                           adjective3=adjective3,
                           adjective4=adjective4)
                          

if __name__ == '__main__':
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True)
