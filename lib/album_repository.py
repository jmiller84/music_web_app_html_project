from lib.album import Album
from lib.artist import Artist

class AlbumRepository:
    # We initialise with a database connection
    def __init__(self, connection):
        self._connection = connection

    # Retrieve all albums
    def all(self):
        rows = self._connection.execute('SELECT * from albums')
        albums = []
        for row in rows:
            item = Album(row["id"], row["title"], row["release_year"], row["artist_id"])
            albums.append(item)
        return albums

    # Find a single album by its id
    def find(self, album_id):
        rows = self._connection.execute(
            'SELECT * from albums WHERE id = %s', [album_id])
        row = rows[0]
        return Album(row["id"], row["title"], row["release_year"], row["artist_id"])

    # Create a new album
    # Do you want to get its id back? Look into RETURNING id;
    def create(self, album):
        self._connection.execute('INSERT INTO albums (title, release_year, artist_id) VALUES (%s, %s, %s)', [
                                 album.title, album.release_year, album.artist_id])
        return None

    # Delete a album by its id
    def delete(self, album_id):
        self._connection.execute(
            'DELETE FROM albums WHERE id = %s', [album_id])
        return None
    
    # Find artist with album_id
    def find_artist_by_album_id(self, album_id):
        rows = self._connection.execute(
            'SELECT albums.id AS album_id, artists.id AS artist_id, artists.name AS artist_name, artists.genre AS artist_genre '\
            'FROM albums '\
            'JOIN artists_albums ON albums.id = artists_albums.album_id '\
            'JOIN artists ON artists.id = artists_albums.artist_id '\
            'WHERE albums.id = %s;', [album_id]
            )
        
        row = rows[0]
        return Artist(row["artist_id"], row["artist_name"], row["artist_genre"])
