from lib.album import Album

"""
Given an id, title, release year and artist id
The album should initiate with those properties
"""
def test_album_initiates():
    album = Album(1, 'Post Human', 2024, 2)
    assert album.id == 1
    assert album.title == 'Post Human'
    assert album.release_year == 2024
    assert album.artist_id == 2

def test_equality():
    album1 = Album(1, 'Post Human', 2024, 2)
    album2 = Album(1, 'Post Human', 2024, 2)
    assert album1 == album2

def test_displays_nicely():
    album = Album(1, 'Post Human', 2024, 2)
    assert str(album) == 'Album(1, Post Human, 2024, 2)'