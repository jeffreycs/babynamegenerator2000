from flask import Flask
import random
app = Flask(__name__)

@app.route("/")
def babyname():
    x = random.randint(1, 100)
    y = random.randint(1, 100)

    title = "<b>BABY NAME GENERATOR 2000 v2.0.6</b><br /><br />"
    code = "<b>" + str(x) + str(y) + "</b><br />"

    if x is y:
        baby = "<br /><br /><img src=https://i.imgur.com/OXnSDWE.jpg />"
    if x is not y:
        baby = "<br /><br /><img src=https://i.imgur.com/Vr3akrM.jpg />"

    return title + "Your unique visitor ID is " + code + "You should name your baby:" + baby

if __name__ == "__main__":
    app.run()
