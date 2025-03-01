from flask import Flask, render_template
from livereload import Server

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run()
