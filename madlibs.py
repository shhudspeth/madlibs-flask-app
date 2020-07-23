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
    play_game = request.args.get("yes")
    name = request.args.get('person')
    compliment = request.args.get('compliment')

    if play_game == "yes":
        return render_template("game.html", name=name, compliment=compliment)
    else:
        return render_template("goodbye.html", name=name)

@app.route("/madlibs")
def show_madlib():
    check_boxes = []
    for key in request.args:
         if str(key).startswith("plural_noun"):
             check_boxes.append(request.args[key])
   
    madlib_choices = {}
    madlib_choices['name'] = request.args.get("name")
    madlib_choices['noun'] = request.args.get('noun')
    madlib_choices['person'] = request.args.get('person')
    madlib_choices['color'] = request.args.get('color')
    madlib_choices['adj'] = request.args.get("adj")
    madlib_choices['plural_nouns'] = check_boxes
    madlib_choices['adverb'] = request.args.get('adverb')
   
    return render_template("madlibs.html",choices_dict=madlib_choices)





if __name__ == '__main__':
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True, host="0.0.0.0")
