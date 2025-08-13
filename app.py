from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    response = None
    if request.method == "POST":
        url = request.form.get("url")
        try:
            r = requests.get(url, timeout=5)
            response = r.text
        except Exception as e:
            response = f"Error: {e}"
    return render_template("home.html", response=response)

@app.route("/about")
def about():
    return render_template("about.html")