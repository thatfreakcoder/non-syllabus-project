from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/syllabus')
def syllabus():
    return render_template('syllabus.html')

@app.route('/available')
def available():
    return render_template('available.html')

@app.route('/request')
def request():
    return render_template('request.html')

@app.route('/upload')
def upload():
    return render_template('upload.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)