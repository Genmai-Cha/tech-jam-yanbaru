from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
	name = "who"

	return render_template('layout.html', name=name)

@app.route('/detail')
def hello2():
	name = "hoge"

	return render_template('detail.html', name=name)

@app.route('/qpost')
def hello3():
	name = "fuga"

	return render_template('q_post.html', name=name)

@app.route('/edit')
def hello4():
	name = "piyo"

	return render_template('editing.html', name=name)

@app.route('/apost')
def hello5():
	name = "poyo"

	return render_template('a_post.html', name=name)

@app.route('/aedit')
def hello6():
	name = "hogehoge"

	return render_template('a_editing.html', name=name)

if __name__ == "__main__":
	app.run(debug=True, port=8888, threaded=True)