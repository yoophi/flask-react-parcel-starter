from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pages/one')
def page_one():
    return render_template('pages/one.html')

@app.route('/pages/two')
def page_two():
    return render_template('pages/two.html')
