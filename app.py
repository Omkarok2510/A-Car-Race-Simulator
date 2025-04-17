from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

# Global car state
cars = [
    {"name": "Lightning", "position": 0, "fuel": 100, "boosts": 2},
    {"name": "Storm", "position": 0, "fuel": 100, "boosts": 2},
    {"name": "Blaze", "position": 0, "fuel": 100, "boosts": 2}
]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/race")
def race():
    winner = None
    for car in cars:
        if car["fuel"] <= 0:
            continue

        if random.random() < 0.2 and car["fuel"] >= 20 and car["boosts"] > 0:
            step = random.randint(20, 30)
            car["fuel"] -= 20
            car["boosts"] -= 1
        else:
            step = random.randint(5, 15)
            car["fuel"] -= random.randint(5, 10)

        car["position"] += step

        if car["position"] >= 100:
            winner = car["name"]

    return jsonify({"cars": cars, "winner": winner})

if __name__ == "__main__":
    app.run(debug=True)
