from flask import Flask, render_template
app = Flask(__name__)


projects = [
    {
        "name": "habit tracker",
        "thumb": "img/habit-tracking.png",
        "hero": "img/habit-tracking-hero.png",
        "categories": ["python", "web"],
        "slug": "habit-tracking",
        "prod": "",
    },
    {
        "name": "personal finance",
        "thumb": "img/personal-finance.png",
        "hero": "img/habit-tracking-hero.png",
        "categories": ["react", "javascript"],
        "slug": "habit-tracking",
        "prod": "",
    },
    {
        "name": "rest-api-docs",
        "thumb": "img/rest-api-docs.png",
        "hero": "img/habit-tracking-hero.png",
        "categories": ["python", "web"],
        "slug": "habit-tracking",
        "prod": "",
    }
]



@app.route("/")
def home():
    return render_template("home.html", projects=projects)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__=="__main__":
    app.run(debug=True)