from flask import Flask,render_template,request
# from models.models import OnegaiContent

#Flaskオブジェクトの生成
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


#「/index」へアクセスがあった場合に、「index.html」を返す
# @app.route("/index")
# def index():
#     name = request.args.get("name")
#     #以下を変更
#     all_onegai = OnegaiContent.query.all()
#     return render_template("jinja.html",name=name,all_onegai=all_onegai)

# @app.route("/index",methods=["post"])
# def post():
#     name = request.form["name"]
#     #ここも変更
#     all_onegai = OnegaiContent.query.all()
#     return render_template("jinja.html", name=name, all_onegai=all_onegai)
#     #変更終わり


#app.pyをターミナルから直接呼び出した時だけ、app.run()を実行する
if __name__ == "__main__":
    app.run(debug=True)