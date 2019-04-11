from flask import Flask, request, redirect, render_template

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('index.html', 
        title="User Sign-Up")

@app.route("/", methods=['POST'])
def check():
    user = request.form['username']
    pword = request.form['password']
    vpword = request.form['verify_password']
    mail = request.form['email']

    u_error = ''
    p_error = ''
    v_error = ''
    e_error = ''

    if not user:
        u_error = 'Please enter in a username'
    elif len(user) < 3 or len(user) > 20:
        u_error = 'Username must be between 3-20 characters long'

    if not pword:
        p_error = 'Please enter in a password'
    elif len(pword) < 3 or len(pword) > 20:
        p_error = 'Password must be between 3-20 characters long'

    if not vpword:
        v_error = 'Please confirm password'
    elif vpword != pword:
        v_error = 'Passwords do not match'

    if not mail:
        e_error = ''
    elif len(mail) < 3 or len(mail) > 20:
        e_error = 'Email must be between 3-20 characters long'
    elif not check_email(mail):
        e_error = 'Please enter in a valid email'

    if not u_error and not p_error and not v_error and not e_error:
        return redirect('/welcome?user={0}'.format(user))
    else:
        return render_template('index.html', 
            title="User Sign-Up",
            username_error=u_error,
            password_error=p_error,
            vpassword_error=v_error,
            email_error = e_error,
            un=user,
            em=mail)

def check_email(email):
    if email.count('@') > 1 or email.count('@') == 0:
        return False
    elif email.count('.') > 1 or email.count('.') == 0:
        return False
    elif email.count(' ') > 0:
        return False
    else:
        return True

@app.route("/welcome")
def welcome():
    name = request.args.get('user')
    
    return render_template("welcome.html", 
        title = "Welcome!",
        username_welcome = name)

app.run()