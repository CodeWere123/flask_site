from flask import Flask, url_for, request, redirect, render_template

from use_db import anti_sqli, reg_account, login_user

app = Flask(__name__)

IS_LOGGED = ""


@app.route('/')
def greeting():
    return render_template('index.html')
@app.route('/hacker')
def hack_attemped():

    return render_template('hacker.html')
@app.route('/login', methods=['POST', 'GET'])
def login():
    global IS_LOGGED
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        print(password, username)
        if not anti_sqli(username, password):
            return redirect("/hacker")
        else:
            is_ok = login_user(username, password)
            if is_ok:
                IS_LOGGED = username
                return redirect(f"/user/{username}")
            else:
                return render_template('incorrect.html')

@app.route('/register', methods=['POST', 'GET'])
def reg():
    global IS_LOGGED
    if request.method == 'GET':
        return render_template('reg_acc.html')
    elif request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        print(password, username)
        if not anti_sqli(username, password):
            return redirect("/hacker")
        else:
            is_ok = reg_account(username, password)
            if is_ok:
                IS_LOGGED = username
                return redirect(f"/user/{username}")
            else:
                return render_template('incorrect2.html')
@app.route('/register', methods=['POST', 'GET'])
def reg():
    global IS_LOGGED
    if request.method == 'GET':
        return render_template('reg_acc.html')
    elif request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        print(password, username)
        if not anti_sqli(username, password):
            return redirect("/hacker")
        else:
            is_ok = reg_account(username, password)
            if is_ok:
                IS_LOGGED = username
                return redirect(f"/user/{username}")
            else:
                return render_template('incorrect2.html')
if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
