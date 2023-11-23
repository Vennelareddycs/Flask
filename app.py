from flask import Flask, render_template

app = Flask(__name__)

@app.route("/first")
def hello_world():
    return  render_template("jinja_intro.html",name="Bob Smith",template_name="Jinja")

@app.route("/second")
def hello_world_fancy():
    return  render_template("second_page.html")

@app.route("/expression")
def render_expression():
    #interpolation
    color= "brown"
    animal_one= "fox"
    animal_two = "dog"

    orange_count = 30 
    apple_count = 20
    donate_amount = 15

    first_name = "Captain"
    last_name="Marvel"

    kwargs = {
        "color": color,
        "animal_one": animal_one,
        "animal_two": animal_two,
        "orange_amount": orange_count,
        "apple_amount": apple_count,
        "donate_amount": donate_amount,
        "first_name": first_name,
        "last_name": last_name,
    }
    return  render_template("expressions.html", **kwargs)

# define custom data structure with a class
class GalileanMoons:
    def __init__(self, first, second, third, fourth):
        self.first = first
        self.second = second
        self.third = third
        self.fourth = fourth

@app.route("/data-structure")
def render_data_structures():

     # list operations
    movies = [
        "Leon the Professional",
        "The Usual Suspects",
        "A Beautiful Mind"
    ]

    # dictionary operations
    car = {
        "brand": "Tesla",
        "model": "Roadstar",
        "year": "2020",
    }

    # custom data structure operations
    moons = GalileanMoons("Io", "Europa", "Ganymede", "Callisto")

    kwargs = {
        "movies": movies,
        "car" : car,
        "moons" : moons,
    }
    return render_template("data_structure.html", **kwargs)

@app.route("/conditionals")
def render_conditionals():
    company = "Micro"
    return render_template("conditionals.html", company=company)


@app.route("/for-loop")
def render_for_loops():
    planets = [
        "Mercury",
        "Venus",
        "Earth",
        "Mars",
        "Jupyter",
        "Saturn",
        "Uranus",
        "Neptune", 
    ]
    return render_template("for_loop.html", planets=planets)

@app.route("/for-loop-dict")
def render_for_loops_dict():
    fruits={
        "apple":"orange",
        "kiwi":"pomegranate",
        "pine":"pineapple"
    }
    return render_template("for_loop_dict.html", fruits=fruits)