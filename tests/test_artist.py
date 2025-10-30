from lib.artist import Artist

def test_artist_initiates():
    artist = Artist(1, "Taylor Swift", 'Pop')
    assert artist.id == 1
    assert artist.name == "Taylor Swift"
    assert artist.genre == "Pop"

def test_artist_comparison():
    artist1 = Artist(1, "Taylor Swift", 'Pop')
    artist2 = Artist(1, "Taylor Swift", 'Pop')
    assert artist1 == artist2

def test_artist_displays_nicely():
    artist = Artist(1, "Taylor Swift", 'Pop')
    assert str(artist) == "Artist(1, Taylor Swift, Pop)"
