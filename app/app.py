from flask import Flask,render_template,request,url_for,redirect
from models.models import Questions
from models.database import db_session

#Flaskオブジェクトの生成
app = Flask(__name__)


@app.route('/')
def top():
	name = "who"

	return render_template('layout.html', name=name)

@app.route('/questions/<int:question_id>')
def question_detail():
	name = "hoge"

	return render_template('detail.html', name=name)

@app.route('/question/form')
def question_form():
    return render_template('question_new.html')

@app.route('/question/new',methods=['post'])
def question_new():
    question_title = request.form["question_title"]
    question_content = request.form["question_content"]
    question = Questions()
    question.title = question_title
    question.content = question_content
    db_session.add(question)
    db_session.commit()
	
    return redirect(url_for('top'))

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
