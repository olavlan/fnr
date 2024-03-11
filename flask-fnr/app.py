from flask import Flask, render_template, request
import requests

FASTAPI_URL = "http://fastapi-app:8000"

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_input = request.form["user_input"]
        response = requests.get(f"{FASTAPI_URL}/validate/{user_input}")
        data = response.json()
        return render_template("index.html", output=data)
    return render_template("index.html", output="")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)