from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def greeting():
    return "HELLO WORLD"

# おまじない
if __name__ == "__main__":
    app.run(debug=True)