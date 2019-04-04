from flask import Flask, request, render_template
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/welcome")
def welcome():
    user = request.form.get('username')
    passw = request.form.get('password')
    vpass = request.form.get('verify_password')
    email = request.form.get('email')


    return render_template('welcome.html', title="user")

app.run()