from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def welcome():
    return 'Welcome on my wonderful Front application !'

@app.route('/login')
def login():
    return 'login'

@app.route('/hello')
@app.route('/hello/<name>')
def hello_world(name="Thierry"):
    return render_template("hello.html", name = name)

app.run()
