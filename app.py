import time
from flask import Flask
import interface

app = Flask(__name__)
cube = interface.Cube()


@app.route("/")
def hello():
    return "lightcube service"


@app.route("/flip")
def flip_info():
    return "/flip/LED on/off"


@app.route("/flip/<led>")
def flip(led):
    x = cube.write(led)
    return "flip %s = %s" % (led, str(x))


@app.route("/alarm/<led>")
def alarm(led):
    for i in range(14):
        cube.write(led)
        time.sleep(0.1)
    return "alarm delivered"
