from lib.album_repository import AlbumRepository
from lib.album import Album
from lib.artist import Artist

"""
When we call AlbumRepository#all
We get a list of Album objects reflecting the seed data.
"""
def test_get_all_records(db_connection): # See conftest.py to learn what `db_connection` is.
    db_connection.seed("seeds/music_web_app.sql") # Seed our database with some test data
    repository = AlbumRepository(db_connection) # Create a new AlbumRepository

    albums = repository.all() # Get all albums

    # Assert on the results
    assert albums == [
        Album(1, 'Legend', 1984, 1),
        Album(2, 'Moonwalker', 1990, 2),
        Album(3, 'Bad', 1993, 2),
    ]

"""
When we call AlbumRepository#find
We get a single Album object reflecting the seed data.
"""
def test_get_single_record(db_connection):
    db_connection.seed("seeds/music_web_app.sql")
    repository = AlbumRepository(db_connection)

    album = repository.find(3)
    assert album == Album(3, 'Bad', 1993, 2)

"""
When we call AlbumRepository#create
We get a new record in the database.
"""
def test_create_record(db_connection):
    db_connection.seed("seeds/music_web_app.sql")
    repository = AlbumRepository(db_connection)

    repository.create(Album(None, "Test Album", 2023, 3))

    result = repository.all()
    assert result == [
        Album(1, 'Legend', 1984, 1),
        Album(2, 'Moonwalker', 1990, 2),
        Album(3, 'Bad', 1993, 2),
        Album(4, "Test Album", 2023, 3)
    ]

"""
When we call AlbumRepository#delete
We remove a record from the database.
"""
def test_delete_record(db_connection):
    db_connection.seed("seeds/music_web_app.sql")
    repository = AlbumRepository(db_connection)
    repository.delete(3) # Apologies to Maggie Nelson fans

    result = repository.all()
    assert result == [
        Album(1, 'Legend', 1984, 1),
        Album(2, 'Moonwalker', 1990, 2)
    ]

"""
When we call find_artist_by_album_id we return an Artist object
"""
def test_find_artist_by_album_id(db_connection):
    db_connection.seed("seeds/music_web_app.sql")
    repository = AlbumRepository(db_connection)
    single_album = repository.find_artist_by_album_id(1)

    assert single_album == Artist(1, 'Pixies', 'Indie')
