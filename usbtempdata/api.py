from flask import Flask

app = Flask(__name__)


@app.route("/ping")
def hello():
    return "pong"


@app.route("/")
def get_graph():
    contents = "null"
    with open("data/graph.html", "r") as graph:
        contents = graph.read()
    return contents


if __name__ == "__main__":
    app.run(host='0.0.0.0')
