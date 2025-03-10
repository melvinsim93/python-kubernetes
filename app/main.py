from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello I Melvin, this is Version 1.1!\n"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
