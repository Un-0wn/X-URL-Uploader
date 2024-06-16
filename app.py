from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'd0st'


if __name__ == "__Bot__":
    app.run()
