DROP TABLE IF EXISTS gametitle;

CREATE TABLE gametitle (
  game_id INTEGER NOT NULL PRIMARY KEY autoincrement,
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

drop table if exists test1;

create table test1(
    game_id integer primary key autoincrement,
    title text not null,
    description text not null
);

drop table if exists test2;

create table test2(
    game_id integer primary key autoincrement,
    title text not null,
    description text not null
);

drop table if exists test3;

create table test3(
    game_id integer primary key autoincrement,
    title text not null,
    description text not null
);

drop table if exists final;

create table final(
    game_id integer primary key autoincrement,
    title text not null,
    description text not null
);

