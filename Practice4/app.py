from flask import Flask, render_template, flash, request, url_for, redirect
from jinja2 import Template, FileSystemLoader, Environment
 
domain = "0.0.0.0:5000/"
templates = FileSystemLoader('templates')
environment = Environment(loader = templates)

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/getSongs", methods=["GET"])
def getAllSongs():
    pass

@app.route("/AddToList", methods="POST")
def addList():
    pass

@app.route("/playNow", methods=["GET"])
def playNow():
    pass

@app.route("/playNext", methods=["GET"])
def playNext():
    pass

@app.route("/playPrevious", methods=["GET"])
def playPrevious():
    pass

if __name__ == "__main__":
    app.run(host="0.0.0.0", port = 8000, debug=True)