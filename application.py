from flask import Flask
from flask import render_template


app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")


@app.route("/heartrate")
def heartrate():
	return render_template("heartrate.html")


if __name__ == "__main__":
	app.run()