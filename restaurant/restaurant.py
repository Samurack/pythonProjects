from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Restaurant"

# get user zip
# get list of restaurants in that area
# check menus for anything with keyword