import sqlite3, random
from flask import Flask, render_template, request, url_for, flash, redirect, abort

app = Flask(__name__)
app.config['SECRET_KEY'] = 'longRandomString'

def get_db_connection():
  conn = sqlite3.connect('database.sqlite')
  conn.row_factory = sqlite3.Row
  return conn

def view_game(game_id):
   conn = get_db_connection()
   game = conn.execute('SELECT * FROM gamedeveloper AS b JOIN gametitle AS a ON a.dev_id = b.dev_id WHERE game_id = ?',
                        (game_id,)).fetchone()
   conn.close()
   if game is None:
        abort(404)
   return game

def get_game(game_id):
    conn = get_db_connection()
    game = conn.execute('SELECT * FROM gametitle WHERE game_id = ?',
                        (game_id,)).fetchone()
    conn.close()
    if game is None:
        abort(404)
    return game

@app.route('/')
def index():
  conn = get_db_connection()
  games = conn.execute('SELECT * FROM gametitle').fetchall()
  conn.close()
  return render_template('index.html', games=games)

@app.route('/addgame/', methods=('GET', 'POST'))
def addgame():
  if request.method == 'POST':
    title = request.form['title']
    genre = request.form['genre']
    description = request.form['description']
    dev_id = request.form['dev_id']
    price = request.form['price']

    if not title:
      flash('Title is required!')
    elif not genre:
      flash('Genre is required')
    elif not price:
      flash('Price is required')
    elif not description:
      flash('Description is required!')
    else:
      conn = get_db_connection()
      #Here I try to auto increment game id and dev id, 
      # but that won't work because you can't USE values from the table without flask alchemy.
      #Right now a blank game or dev id will crash the website, but i'm leaving this as a reminder.
      
      # if not game_id:
      #   game_id = conn.execute('SELECT max(game_id) FROM gametitle').fetchone()
      #   game_id = game_id + 1
      # if not game_id:
      #   dev_id = conn.execute('SELECT max(dev_id) FROM gametitle').fetchone()
      #   dev_id = dev_id + 1
      
      #this works fine, but the price is displayed strangely
      addTable = random.randint(0,4)
      conn.execute('INSERT INTO gametitle (title, genre, description, dev_id, price) VALUES (?,?,?,?,?)',
                    (title, genre, description, dev_id, round(float(price), 2)))
      if addTable == 1:
        conn.execute('insert into test1 (title,description) values (?,?)', (title, description))
      elif addTable == 2: 
        conn.execute('insert into test2 (title,description) values (?,?)', (title, description))
      elif addTable == 3:
        conn.execute('insert into test3 (title,description) values (?,?)', (title, description))
      elif addTable == 4:
        conn.execute('insert into final (title,description) values (?,?)', (title, description))
                  
      
      conn.commit()
      conn.close()
      return redirect(url_for('index'))
    
  return render_template('addgame.html')

@app.route('/<int:game_id>/edit/', methods=('GET', 'POST'))
def edit(game_id):
    game = get_game(game_id)

    if request.method == 'POST':
        title = request.form['title']
        genre = request.form['genre']
        description = request.form['description']
        dev_id = request.form['dev_id']
        price = request.form['price']

        if not title:
          flash('Title is required!')
        elif not genre:
          flash('Genre is required')
        elif not price:
          flash('Price is required')
        elif not description:
          flash('Description is required!')

        else:
            conn = get_db_connection()
            conn.execute('UPDATE gametitle SET game_id = ?, title = ?, genre = ?, description = ?, dev_id = ?, price = ?'
                         ' WHERE game_id = ?',
                         (title, genre, description, dev_id, price, game_id))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))

    return render_template('edit.html', game=game)

@app.route('/<int:game_id>/delete/', methods=('POST',))
def delete(game_id):
    game = get_game(game_id)
    conn = get_db_connection()
    conn.execute('DELETE FROM gametitle WHERE game_id = ?', (game_id,))
    conn.commit()
    conn.close()
    flash('"{}" was successfully deleted!'.format(game['title']))
    return redirect(url_for('index'))

@app.route('/<int:game_id>/view/', methods=('GET','POST'))
def view(game_id):
    game = view_game(game_id)
    # conn = get_db_connection()
    # conn.execute('SELECT * FROM gamedeveloper join gametitle ', (game_id,))
    # conn.commit()
    # conn.close()
    # games = conn.execute('SELECT * FROM gametitle').fetchall()
    # conn.close()
    #return render_template('index.html', game=game)
    return render_template('view.html', game=game)


@app.route('/test_1/')
def test_1():
    conn = get_db_connection()
    games = conn.execute('select * from test1').fetchall()
    conn.close()
    return render_template('test_1.html', games=games)

@app.route('/test_2/')
def test_2():
    conn = get_db_connection()
    games = conn.execute('select * from test2').fetchall()
    conn.close()
    return render_template('test_2.html', games=games)

@app.route('/test_3/')
def test_3():
    conn = get_db_connection()
    games = conn.execute('select * from test3').fetchall()
    conn.close()
    return render_template('test_3.html', games=games)
@app.route('/final/')
def final():
    conn = get_db_connection()
    games = conn.execute('select * from final').fetchall()
    conn.close()
    return render_template('final.html', games=games)


