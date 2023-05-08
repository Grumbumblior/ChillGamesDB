import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
  connection.executescript(f.read())

cur = connection.cursor()

cur.execute(
  "INSERT INTO gametitle (game_id, title, genre, description, dev_id, price) VALUES (?,?,?,?,?,?)",
  (1, 'A Short Hike', 'Exploration',
   'Hike, climb, and soar through the peaceful mountainside landscapes of Hawk Peak Provincial Park as you make your way to the summit.',
   1, 7.99))

cur.execute(
  "INSERT INTO gametitle (game_id, title, genre, description, dev_id, price) VALUES (?,?,?,?,?,?)",
  (2, 'Stardew Valley', 'Farming Sim',
   "You've inherited your grandfather's old farm plot in Stardew Valley. Armed with hand-me-down tools and a few coins, you set out to begin your new life. Can you learn to live off the land and turn these overgrown fields into a thriving home?",
   2, 14.99))

connection.commit()
connection.close()
