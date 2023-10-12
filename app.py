import os
from flask import Flask, request, render_template, redirect
from lib.database_connection import get_flask_database_connection
from lib.album_repository import AlbumRepository
from lib.album import Album
from lib.artist_repository import ArtistRepository
from lib.artist import Artist


# Create a new Flask app
app = Flask(__name__)


# -------- ROUTES ALBUMS-----------

# # POST /albums
# # with body paramaters: title=Voyage, release_year=2022, artist_id=2
# @app.route('/albums', methods = ['POST'])
# def create_album():
#     if has_invalid_album_parameters(request.form):
#         return "You need to submit a title, release_year, and artist_id", 400
#     connection = get_flask_database_connection(app)
#     repository = AlbumRepository(connection)
#     title = request.form['title']
#     release_year = request.form['release_year']
#     artist_id = request.form['artist_id']

#     new_album = Album(None, title, release_year, artist_id)
#     repository.create(new_album) 
#     return '', 200
 


# POST /albums
@app.route('/albums', methods = ['POST'])
def create_album():
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)

    title = request.form['title']
    release_year = request.form['release_year']
    artist_id = request.form['artist_id']
    new_album = Album(None, title, release_year, artist_id)

    if not new_album.is_valid():
        errors = new_album.generate_errors()
        return render_template("albums/new_album.html", errors= errors)


    repository.create(new_album) 

    return redirect(f"/albums/{new_album.id}")


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
    # artist = repository.find_artist_by_album_id(id)

    return render_template('albums/single_album.html' , album=album)

def has_invalid_album_parameters(form):
    return 'title' not in form or \
        'release_year' not in form \
        or 'artist_id' not in form 


#GET /albums/new
@app.route('/albums/new')
def get_book_new():
    return render_template('albums/new_album.html')

#POST /albums



# --------------ROUTES ARTISTS -------  
#       
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
@app.route("/artists", methods = ['POST'])
def create_artist():
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)

    name = request.form['name']
    genre = request.form['genre']
    new_artist = Artist(None, name, genre)

    if not new_artist.is_valid():
        errors = new_artist.generate_errors()
        return render_template("artists/new_artist.html", errors=errors)

    repository.create(new_artist)

    return redirect(f"/artists/{new_artist.id}")


#GET /artists/new_artist
@app.route('/artists/new_artist')
def get_artist_new():
    return render_template('artists/new_artist.html')


# @app.route('/artists', methods = ['POST'])
# def post_artists():
#     if has_invalid_artist_parameters(request.form):
#         return "You need to submit a name and a genre", 400
#     connection = get_flask_database_connection(app)
#     repository = ArtistRepository(connection)
#     name = request.form['name']
#     genre = request.form['genre']

#     new_artist = Artist(None, name, genre)
#     repository.create(new_artist)
#     return '', 200
    
# def has_invalid_artist_parameters(form):
#     return 'name' not in form or \
#         'genre' not in form


# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
