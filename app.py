
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, World theises has been hy delivered on time !"