import os
from flask import Flask, request, render_template, redirect
from lib.database_connection import get_flask_database_connection
from lib.album_repository import AlbumRepository
from lib.artist_repository import ArtistRepository
from lib.album import Album
from lib.artist import Artist

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==


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


@app.route('/albums', methods=['POST'])
def create_albums():
    conn = get_flask_database_connection(app)
    title = request.form['title']
    release_year = int(request.form['release-year'])
    repo = AlbumRepository(conn)
    # No artist id until functionality is added
    album = repo.add(Album(None, title, release_year, None))
    return redirect(f"/albums/{album.id}")

@app.route('/albums')
def get_all_albums():
    conn = get_flask_database_connection(app)
    repo = AlbumRepository(conn)
    albums = repo.all()
    return render_template("albums/index.html", albums=albums)

@app.route('/albums/new')
def add_album():
    return render_template("albums/new.html")

@app.route('/albums/<int:id>')
def get_album(id):
    conn = get_flask_database_connection(app)
    repo = AlbumRepository(conn)
    album = repo.find(id)
    print(album)
    return render_template("albums/show.html", album=album)

@app.route('/artists')
def get_all_artists():
    conn = get_flask_database_connection(app)
    repo = ArtistRepository(conn)
    artists = repo.all()
    return '\n'.join([f"{artist}" for artist in artists])

@app.route('/artists', methods=['POST'])
def create_artist():
    conn = get_flask_database_connection(app)
    repo = ArtistRepository(conn)
    name = request.form['name']
    genre = request.form['genre']
    repo.add(Artist(None, name, genre))
    return 'Success', 200


# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
