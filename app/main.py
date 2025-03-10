from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello I am Melvin, this is Version 3!\n"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
