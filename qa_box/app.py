from flask import Flask
app = Flask(__name__)

@app.route('/')
def greeting():
    return "HELLO WORLD"

# おまじない
if __name__ == "__main__":
    app.run(debug=True)