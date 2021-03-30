from flask import Flask,render_template,request,url_for,redirect,jsonify
from models.models import Questions, Comments
from models.database import db_session

#Flaskオブジェクトの生成
app = Flask(__name__)


@app.route('/')
def top():
	name = "who"

	return render_template('layout.html', name=name)

@app.route('/questions/<int:question_id>')
def question_detail(question_id):
	question = Questions.query.filter_by(id=question_id).first()

	return render_template('question_detail.html', question=question)

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

@app.route('/question/<int:question_id>/edit',methods=['post'])
def question_edit(question_id):
    question = Questions.query.filter_by(id=question_id).first()
    question.title = request.args.get("question_title")
    question.content = request.args.get("question_content")
    db_session.add(question)
    db_session.commit()

    return redirect(url_for('question_detail', question_id=question_id))

@app.route('/questions/<int:question_id>/comments/new')
def get_questions_comments_new(question_id):
    return render_template('question_comment_new.html', question_id=question_id)

@app.route('/comments', methods=['post'])
def post_comments():
    comment = Comments()
    comment.question_id = request.form['question_id']
    comment.content = request.form['content']
    db_session.add(comment)
    db_session.commit()

    return redirect(url_for('question_detail', question_id=comment.question_id))

@app.route('/answers/<int:question_id>')
def answer_edit():
	name = "hogehoge"

	return render_template('a_editing.html', name=name)
