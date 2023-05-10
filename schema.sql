DROP TABLE IF EXISTS gametitle;

CREATE TABLE gametitle (
  game_id INTEGER NOT NULL PRIMARY KEY,
  title VARCHAR(50) NOT NULL,
  genre VARCHAR(30) DEFAULT NULL,
  description TEXT DEFAULT NULL,
  dev_id INTEGER DEFAULT NULL,
  price FLOAT DEFAULT NULL
  );
DROP TABLE IF EXISTS gamedeveloper;

CREATE TABLE gamedeveloper(
  dev_id INTEGER NOT NULL PRIMARY KEY,
  dev_name TEXT DEFAULT NULL
);

SELECT * FROM gamedeveloper JOIN gametitle ON dev_id WHERE game_id = 1;

