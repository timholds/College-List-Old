
from flask import render_template
from app import app

"""
@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")
"""

@app.route('/')
def nomad_homepage():
    return render_template('templates/index.html')

@app.route('/')
@app.route('/index')
def show_entries():
    db = get_db()
    cur = db.execute('select title, text from entries order by id desc')
    entries = cur.fetchall()
    return render_template('templates/show_entries.html', entries=entries)

@app.route('/add', methods=['POST'])
def add_entry():
    if not session.get('logged_in'):
        abort(401)
    db = get_db()
    db.execute('insert into entries (title, text) values (?, ?)',
                 [request.form['title'], request.form['text']])
    db.commit()
    flash('New entry was successfully posted')
    return redirect(url_for('show_entries'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('show_entries'))
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('show_entries'))

@app.route('/UCLA')
def ucla():
    #TODO make UCLA.html
    return render_template('UCLA.html')

@app.route('/Berkeley')
def berkeley():
    return render_template('Berkeley.html')

@app.route('/Irvine')
def irvine():
    return render_template('Irvine.html')