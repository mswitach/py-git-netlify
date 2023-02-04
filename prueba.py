from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hola, marce!"

if __name__ == "__main__":
    app.run()

