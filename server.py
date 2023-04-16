from flask import Flask
import random


app = Flask(__name__)


@app.route("/")
def guess_number():
    return "<h1>Guess a number between 0 and 9</h1>" \
           "<img src='https://media.giphy.com/media/MZQkUm97KTI1gI8sUj/giphy.gif' alt='a_gif_of_a_man_thinking'>"


answer = random.randint(0, 9)


@app.route("/<int:guess>")
def check_guess(guess):
    result = ""
    result_gif = ""
    if abs(guess - answer) >= 7:
        result = "too cold"
        result_gif = "https://media.giphy.com/media/xULW8jsQM8wsfqii6k/giphy.gif"
    elif abs(guess - answer) >= 5:
        result = "cold"
        result_gif = "https://media.giphy.com/media/3oFzm7xQje1yyQK3e0/giphy.gif"
    elif abs(guess - answer) >= 3:
        result = "hot"
        result_gif = "https://media.giphy.com/media/ckB5razpgN2rd4qTfe/giphy.gif"
    elif abs(guess - answer) >= 1:
        result = "too hot"
        result_gif = "https://media.giphy.com/media/xT0Gqz4x4eLd5gDtaU/giphy.gif"
    elif abs(guess - answer) == 0:
        result = "You found  me!"
        result_gif = "https://media.giphy.com/media/2m1lj8p8v6JcWpREtL/giphy.gif"

    return f"<h1>{result}</h1>" \
           f"<img src={result_gif}>"


if __name__ == "__main__":
    app.run(debug=True)
    