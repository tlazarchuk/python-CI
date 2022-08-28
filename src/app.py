from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, world!"

@app.route("/home")
def home():
    return "Hello, home!"

@app.route("/profile")
def profile():
    return "It's my profile!"

if __name__ == "__main__":
    app.run()

