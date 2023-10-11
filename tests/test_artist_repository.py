from lib.artist_repository import ArtistRepository
from lib.artist import Artist

"""
When we call ArtistRepository#all
We get a list of Artist objects reflecting the seed data.
"""
def test_get_all_records(db_connection): # See conftest.py to learn what `db_connection` is.
    db_connection.seed("seeds/music_web_app.sql") # Seed our database with some test data
    repository = ArtistRepository(db_connection) # Create a new ArtistRepository

    artists = repository.all() # Get all artists

    # Assert on the results
    assert artists == [
            Artist(1, 'Pixies', 'Indie'),
            Artist(2, 'ABBA', 'Pop'),
            Artist(3, 'Taylor Swift', 'Pop'),
            Artist(4, 'Nina Simone', 'Soul'),
    ]

"""
When we call ArtistRepository#find
We get a single Artist object reflecting the seed data.
"""
def test_get_single_record(db_connection):
    db_connection.seed("seeds/music_web_app.sql")
    repository = ArtistRepository(db_connection)

    artist = repository.find(3)
    assert artist == Artist(3, 'Taylor Swift', 'Pop')

"""
When we call ArtistRepository#create
We get a new record in the database.
"""
def test_create_record(db_connection):
    db_connection.seed("seeds/music_web_app.sql")
    repository = ArtistRepository(db_connection)

    repository.create(Artist(None, "Test Artist", "Pop"))

    result = repository.all()
    assert result == [
        Artist(1, 'Pixies', 'Indie'),
        Artist(2, 'ABBA', 'Pop'),
        Artist(3, 'Taylor Swift', 'Pop'),
        Artist(4, 'Nina Simone', 'Soul'),
        Artist(5, "Test Artist", "Pop")
    ]

"""
When we call ArtistRepository#delete
We remove a record from the database.
"""
def test_delete_record(db_connection):
    db_connection.seed("seeds/music_web_app.sql")
    repository = ArtistRepository(db_connection)
    repository.delete(3) # Apologies to Maggie Nelson fans

    result = repository.all()
    assert result == [
        Artist(1, 'Pixies', 'Indie'),
        Artist(2, 'ABBA', 'Pop'),
        Artist(4, 'Nina Simone', 'Soul'),
    ]
