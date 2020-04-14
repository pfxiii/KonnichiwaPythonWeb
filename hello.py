import flask

app=flask.Flask(__name__)
app.secret_key='pfxiii'
app.debug = True

@app.route('/')
def index():
    namae=flask.session.get('namae')
    hitokoto=flask.session.get('hitokoto')
    return flask.render_template('index.html',namae=namae,hitokoto=hitokoto)

@app.route("/toroku",methods=['POST'])
def toroku():
    namae=flask.request.form['namae']
    hitokoto=flask.request.form['hitokoto']
    flask.session['namae']=namae
    flask.session['hitokoto']=hitokoto
    return flask.render_template('toroku.html',namae=namae,hitokoto=hitokoto)

app.run()
