from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Task list to store tasks
tasks = []

# Login credentials
USERNAME = 'ritika'
PASSWORD = 'tripathi'

@app.route('/')
def homepage():
    if 'logged_in' in session:
        return render_template('index.html', tasks=tasks)
    else:
        return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username == USERNAME and password == PASSWORD:
            session['logged_in'] = True
            return redirect(url_for('homepage'))
        else:
            flash('Invalid login credentials. Please try again.')
            return redirect(url_for('login'))
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('login'))

@app.route('/add-task', methods=['GET', 'POST'])
def add_task():
    if 'logged_in' in session:
        if request.method == 'POST':
            task = request.form.get('task')
            if task:
                tasks.append(task)
            return redirect(url_for('homepage'))
        return render_template('add_task.html')
    else:
        return redirect(url_for('login'))

@app.route('/delete-task', methods=['GET', 'POST'])
def delete_task():
    if 'logged_in' in session:
        if request.method == 'POST':
            task_to_delete = request.form.get('task_to_delete')
            if task_to_delete in tasks:
                tasks.remove(task_to_delete)
            return redirect(url_for('homepage'))
        return render_template('delete_task.html', tasks=tasks)
    else:
        return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)