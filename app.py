import os
from flask import Flask, request, render_template
from lib.database_connection import get_flask_database_connection
from lib.album_repository import AlbumRepository
from lib.album import Album
from lib.artist_repository import ArtistRepository
from lib.artist import Artist


# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

# POST /albums
# with body paramaters: title=Voyage, release_year=2022, artist_id=2
@app.route('/albums', methods = ['POST'])
def post_album():
    if has_invalid_album_parameters(request.form):
        return "You need to submit a title, release_year, and artist_id", 400
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    title = request.form['title']
    release_year = request.form['release_year']
    artist_id = request.form['artist_id']

    new_album = Album(None, title, release_year, artist_id)
    repository.create(new_album)
    return '', 200
 


 # GET /albums
@app.route('/albums', methods=['GET'])
def get_albums():
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)

    albums = repository.all() 
    return render_template("albums/index.html", albums=albums)


# GET /abums/1
@app.route('/albums/<id>')
def get_single_album(id):
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    album = repository.find(id)
    artist = repository.find_artist_by_album_id(id)

    return render_template('albums/single_album.html' , album=album, artist=artist)

def has_invalid_album_parameters(form):
    return 'title' not in form or \
        'release_year' not in form \
        or 'artist_id' not in form 
              
# GET /artists/1
@app.route('/artists/<id>')
def get_single_artist(id):
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)
    artist = repository.find(id)

    return render_template('artists/single_artist.html', artist=artist)

# GET /artists
@app.route("/artists", methods=['GET'])
def get_artists():
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)

    artists = repository.all()
    return render_template('artists/artists.html', artists=artists)


# POST /artists
@app.route('/artists', methods = ['POST'])
def post_artists():
    if has_invalid_artist_parameters(request.form):
        return "You need to submit a name and a genre", 400
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)
    name = request.form['name']
    genre = request.form['genre']

    new_artist = Artist(None, name, genre)
    repository.create(new_artist)
    return '', 200
    
def has_invalid_artist_parameters(form):
    return 'name' not in form or \
        'genre' not in form



# == Example Code Below ==

# GET /emoji
# Returns a smiley face in HTML
# Try it:
#   ; open http://localhost:5001/emoji
@app.route('/emoji', methods=['GET'])
def get_emoji():
    # We use `render_template` to send the user the file `emoji.html`
    # But first, it gets processed to look for placeholders like {{ emoji }}
    # These placeholders are replaced with the values we pass in as arguments
    return render_template('emoji.html', emoji=':)')

# This imports some more example routes for you to see how they work
# You can delete these lines if you don't need them.
from example_routes import apply_example_routes
apply_example_routes(app)

# == End Example Code ==

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
