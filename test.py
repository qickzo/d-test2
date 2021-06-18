from flask import Flask


app = Flask(__name__)

@app.route('/')
def index():
     return '<h1>HEllo</h1>'

@app.route('/home')
def home():
    return "<h2>Now, I am in home</h2>"

app.run(debug=True)