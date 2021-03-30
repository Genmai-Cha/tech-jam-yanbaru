from flask import Flask,render_template,request,url_for,redirect,jsonify
from models.models import Questions, Comments
from models.database import db_session
from sqlalchemy import desc

#Flaskオブジェクトの生成
app = Flask(__name__)


@app.route('/')
def top():
    question_list = Questions.query.order_by(desc(Questions.created_at)).all()
    return render_template('index.html', questions=question_list)

@app.route('/questions/<int:question_id>')
def question_detail(question_id):
	question = Questions.query.filter_by(id=question_id).first()
    # comment = Comments.query.filter_by(id=question_id).first()
    # ,comment_body=comment
	return render_template('question_detail.html', question=question,question_id=question_id)

@app.route('/questions/<int:question_id>/edit')
def question_edit(question_id):
	question = Questions.query.filter_by(id=question_id).first()

	return render_template('question_edit.html', question=question)

@app.route('/questions/<int:question_id>', methods=['patch'])
def patch_question(question_id):
    question = Questions.query.filter_by(id=question_id).first()
    question.title = request.form['question_title']
    question.content = request.form['question_content']
    db_session.add(question)
    db_session.commit()

    return jsonify({
        'id': question.id,
        'title': question.title,
        'content': question.content,
    })

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

@app.route('/comments/<int:comment_id>')
def get_comments_edit(comment_id):
    comment = db_session.query(Comments).filter(Comments.id==comment_id).first()
    return render_template('comment_edit.html', comment=comment)

@app.route('/comments/<int:comment_id>', methods=['patch'])
def patch_comments_edit(comment_id):
    comment = db_session.query(Comments).filter(Comments.id==comment_id).first()
    comment.content = request.form['content']
    db_session.add(comment)
    db_session.commit()

    return jsonify({
        'id': comment.id,
        'question_id': comment.question_id,
        'content': comment.content,
    })
