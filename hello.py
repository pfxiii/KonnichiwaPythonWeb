import flask
import pymysql.cursors

app=flask.Flask(__name__)
app.secret_key='pfxiii'
app.debug = True

connection=pymysql.connect(host='localhost',user='pfxiii',password='pfxiii',db='pfxiii',charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)

@app.route('/')
def index():
    with connection.cursor() as cursor:
        cursor.execute('SELECT * from pfxiii')
        ichiran=cursor.fetchall()
    return flask.render_template('index.html',ichiran=ichiran)

@app.route("/toroku",methods=['POST'])
def toroku():
    namae=flask.request.form['namae']
    hitokoto=flask.request.form['hitokoto']
    with connection.cursor() as cursor:
        cursor.execute('SELECT * FROM pfxiii WHERE namae=%s',(namae))
        kakunin=cursor.fetchone()

    with connection.cursor() as cursor:
        if kakunin:
            cursor.execute('UPDATE pfxiii SET hitokoto=%s WHERE namae=%s',(hitokoto,namae))
            connection.commit()
            return flask.render_template('kosin.html',namae=namae,hitokoto=hitokoto)
        else:
            cursor.execute('INSERT INTO pfxiii(namae,hitokoto) VALUES(%s,%s)',(namae,hitokoto))
            connection.commit()
            return flask.render_template('toroku.html',namae=namae,hitokoto=hitokoto)

@app.route("/sakujo",methods=['POST'])
def sakujo():
    checklist=flask.request.form.getlist("check")
    with connection.cursor() as cursor:
        for namae in checklist:
            cursor.execute('DELETE FROM pfxiii WHERE namae=%s',(namae))
            connection.commit()
    return flask.render_template('sakujo.html')

app.run()