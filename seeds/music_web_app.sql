DROP TABLE IF EXISTS albums CASCADE;
DROP SEQUENCE IF EXISTS albums_id_seq;
DROP TABLE IF EXISTS artists CASCADE;
DROP SEQUENCE IF EXISTS artists_id_seq;
DROP TABLE IF EXISTS artists_albums CASCADE;


-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS albums_id_seq;
CREATE TABLE albums (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    release_year INT,
    artist_id INT
);

CREATE SEQUENCE IF NOT EXISTS artists_id_seq;
CREATE TABLE artists (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    genre VARCHAR(255)
);


CREATE TABLE artists_albums(
    artist_id INT,
    album_id INT,
    constraint fk_album foreign key(album_id) references albums(id) on delete CASCADE,
    constraint fk_artist foreign key(artist_id) references artists(id) on delete CASCADE,
    PRIMARY KEY(artist_id, album_id)
);


INSERT INTO albums (title, release_year, artist_id) VALUES ('Legend', 1984, 1);
INSERT INTO albums (title, release_year, artist_id) VALUES ('Moonwalker', 1990, 2);
INSERT INTO albums (title, release_year, artist_id) VALUES ('Bad', 1993, 2);

INSERT INTO artists (name, genre) VALUES ('Pixies', 'Indie');
INSERT INTO artists (name, genre) VALUES ('ABBA', 'Pop');
INSERT INTO artists (name, genre) VALUES ('Taylor Swift', 'Pop');
INSERT INTO artists (name, genre) VALUES ('Nina Simone', 'Soul');

INSERT INTO artists_albums(artist_id, album_id) VALUES (1, 1);
INSERT INTO artists_albums(artist_id, album_id) VALUES (2, 2);
INSERT INTO artists_albums(artist_id, album_id) VALUES (3, 3);