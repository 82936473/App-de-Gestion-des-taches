from flask import Flask, render_template,request,redirect,url_for,session
from Tasks_Manager import Tasks_Manager as s
app = Flask(__name__)
app.secret_key="Long_random_secret_key"
tasks=None

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html',title='Home')


@app.route('/sign_up',methods=['POST','GET'])
def sign_up():
    print('-------------------sign-------------------')
    error=None
    if request.method=='POST':
        username = request.form.get("username")
        password = request.form.get("password")
        verify = request.form.get("verifypassword")
        try:
            if password!=verify:
                raise ValueError("❌ Passwords do not match")
            s.sign_up(username,password)
            session["username"] = username
            return redirect(url_for('dashboard'))
        except ValueError as e:
            error=str(e)
    return render_template('sign_up.html',title='Sign up',error=error)


@app.route('/log_in',methods=['POST','GET'])
def log_in():
    print('-------------------log-------------------')
    error=None
    if request.method=='POST':
        print('----------------------- pass log_in')
        username = request.form.get("username")
        password = request.form.get("password")
        try:
            s.log_in(username,password)
            session["username"] = username
            return redirect(url_for('dashboard'))
        except ValueError as e:
            error=str(e)
    return render_template('log_in.html',title='Log in',error=error)
@app.route('/dashboard')
def dashboard():
    username=session['username']
    tasks=s.get_tasks(username)
    print(tasks)
    return render_template('dashboard.html',title='Dashboard',tasks=tasks)

if __name__ == "__main__":
    app.run(debug=True)