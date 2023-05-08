import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect

app = Flask(__name__)
app.config['SECRET_KEY'] = 'longRandomString'

def get_db_connection():
  conn = sqlite3.connect('database.db')
  conn.row_factory = sqlite3.Row
  return conn


@app.route('/')
def index():
  conn = get_db_connection()
  games = conn.execute('SELECT * FROM gametitle').fetchall()
  conn.close()
  return render_template('index.html', games=games)

@app.route('/addgame/', methods=('GET', 'POST'))
def addgame():
    return render_template('addgame.html')