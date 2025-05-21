from flask import Flask, render_template, abort
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
        "slug": "personal-finance",
        "prod": "",
    },
    {
        "name": "rest-api-docs",
        "thumb": "img/rest-api-docs.png",
        "hero": "img/habit-tracking-hero.png",
        "categories": ["python", "web"],
        "slug": "rest-api-docs",
        "prod": "",
    }
]
# mapped each slug to the corresponding dictionary containing it 
# this is a very common way of indexing to find things easier
slug_to_project = {project["slug"]: project for project in projects}
@app.route("/")
def home():
    return render_template("home.html", projects=projects)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/project/<string:slug>")
def project(slug):
    if slug not in slug_to_project:
        abort(404)
    else:
        return render_template(f"project_{slug}.html", project=slug_to_project[slug])

@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404





if __name__=="__main__":
    app.run(debug=True)