import sqlite3

connection = sqlite3.connect('database.sqlite')

with open('schema.sql') as f:
  connection.executescript(f.read())

cur = connection.cursor()

cur.execute(
  "INSERT INTO gametitle (game_id, title, genre, description, dev_id, price) VALUES (?,?,?,?,?,?)",
  (1, 'A Short Hike', 'Exploration',
   'Hike, climb, and soar through the peaceful mountainside landscapes of Hawk Peak Provincial Park as you make your way to the summit.',
   1, 7.99))

cur.execute(
  "INSERT INTO test1 (game_id, title, description) VALUES (?,?,?)",
  (1, 'A Short Hike',
   'Hike, climb, and soar through the peaceful mountainside landscapes of Hawk Peak Provincial Park as you make your way to the summit.'))


cur.execute(
  "INSERT INTO gametitle (game_id, title, genre, description, dev_id, price) VALUES (?,?,?,?,?,?)",
  (2, 'Stardew Valley', 'Farming Sim',
   "You've inherited your grandfather's old farm plot in Stardew Valley. Armed with hand-me-down tools and a few coins, you set out to begin your new life. Can you learn to live off the land and turn these overgrown fields into a thriving home?",
   2, 14.99))

cur.execute(
  "INSERT INTO test2 (game_id, title, description) VALUES (?,?,?)",
  (2, 'Stardew Valley',
   "You've inherited your grandfather's old farm plot in Stardew Valley. Armed with hand-me-down tools and a few coins, you set out to begin your new life. Can you learn to live off the land and turn these overgrown fields into a thriving home?",
  ))

cur.execute(
  "INSERT INTO gametitle (game_id, title, genre, description, dev_id, price) VALUES (?,?,?,?,?,?)",
  (3, 'Animal Crossing', 'Social Sim',
   'Escape to a deserted island and create your own paradise as you explore, create, and customize in the Animal Crossing: New Horizons game.',
   3, 59.99))

cur.execute(
  "INSERT INTO test3 (game_id, title, description) VALUES (?,?,?)",
  (3, 'Animal Crossing',
   'Escape to a deserted island and create your own paradise as you explore, create, and customize in the Animal Crossing: New Horizons game.'
   ))

cur.execute(
  "INSERT INTO gametitle (game_id, title, genre, description, dev_id, price) VALUES (?,?,?,?,?,?)",
  (4, 'Legend of Zelda: Breath of the Wild', 'Exploration',
   "Step into a world of discovery, exploration, and adventure in The Legend of Zelda: Breath of the Wild, a boundary-breaking new game in the acclaimed series.",
   4, 59.99))

cur.execute(
  "INSERT INTO final (game_id, title, description) VALUES (?,?,?)",
  (4, 'Legend of Zelda: Breath of the Wild',
   "Step into a world of discovery, exploration, and adventure in The Legend of Zelda: Breath of the Wild, a boundary-breaking new game in the acclaimed series."))


cur.execute(
  "INSERT INTO gamedeveloper (dev_id, dev_name) VALUES (?,?)",
  (1, 'adamgyru'))

cur.execute(
  "INSERT INTO gamedeveloper (dev_id, dev_name) VALUES (?,?)",
  (2, 'ConcernedApe'))

cur.execute(
  "INSERT INTO gamedeveloper (dev_id, dev_name) VALUES (?,?)",
  (3, 'Nintendo'))

cur.execute(
  "INSERT INTO gamedeveloper (dev_id, dev_name) VALUES (?,?)",
  (4, 'Nintendo'))

connection.commit()
connection.close()
