from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, Flask!"

@app.route("/user/<name>")
def greetings(name):
    return f"Hi {name}, welcome my first Flask"



if __name__=="__main__":

    app.run(debug=True)