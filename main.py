from flask import Flask, render_template, request

app = Flask(__name__, template_folder="templates")

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/generate", methods=["POST"])
def generate():
    name = request.form["name"]
    user_id = request.form["user_id"]
    age = request.form["age"]
    weight = request.form["weight"]
    goal = request.form["goal"]
    intensity = request.form["intensity"]

    return f"""
    <html>
    <head>
        <title>FitBuddy Result</title>
    </head>
    <body>
        <h1>FitBuddy - Fitness Plan</h1>

        <h2>Hello {name}!</h2>

        <p><b>User ID:</b> {user_id}</p>
        <p><b>Age:</b> {age}</p>
        <p><b>Weight:</b> {weight} kg</p>
        <p><b>Fitness Goal:</b> {goal}</p>
        <p><b>Workout Intensity:</b> {intensity}</p>

        <h2>Your Fitness Plan</h2>

        <h3>Workout</h3>
        <ul>
            <li>Warm-up - 10 minutes</li>
            <li>Cardio - 20 minutes</li>
            <li>Strength Training - 20 minutes</li>
            <li>Cool-down - 10 minutes</li>
        </ul>

        <h3>Daily Advice</h3>
        <ul>
            <li>Drink enough water</li>
            <li>Get adequate sleep</li>
            <li>Follow a balanced diet</li>
            <li>Exercise regularly</li>
        </ul>

        <br>
        <a href="/">Back to FitBuddy</a>
    </body>
    </html>
    """


if __name__ == "__main__":
    app.run(debug=True)