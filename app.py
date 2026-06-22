from flask import Flask, render_template, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/dashboard')
def view_dashboard():
    return render_template('dashboard.html')

if __name__ == '__main__':    
    app.run(debug=True)