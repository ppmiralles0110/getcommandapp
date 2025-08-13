from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    response = None
    url = None
    if request.method == "POST":
        action = request.form.get("action")
        if action == "clear":
            response = None
            url = ""
        else:
            url = request.form.get("url")
            try:
                r = requests.get(url, timeout=5)
                response = r.text
            except Exception as e:
                response = f"Error: {e}"
    return render_template("home.html", response=response, url=url)

@app.route("/about")
def about():
    return render_template("about.html")