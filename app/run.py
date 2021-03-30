from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def top():
	name = "who"

	return render_template('layout.html', name=name)

@app.route('/questions/<int:question_id>')
def question_detail():
	name = "hoge"

	return render_template('detail.html', name=name)

@app.route('/questions/new')
def question_post():
	name = "fuga"

	return render_template('q_post.html', name=name)

@app.route('/questions/<int:question_id>/edit')
def question_edit():
	name = "piyo"

	return render_template('editing.html', name=name)

@app.route('/answers/new')
def answer_post():
	name = "poyo"

	return render_template('a_post.html', name=name)

@app.route('/answers/<int:question_id>')
def answer_edit():
	name = "hogehoge"

	return render_template('a_editing.html', name=name)

if __name__ == "__main__":
	app.run(debug=True, port=8888, threaded=True)