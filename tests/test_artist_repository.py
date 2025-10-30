from lib.artist_repository import ArtistRepository
from lib.artist import Artist

def test_artist_repo_all(db_connection):
    db_connection.seed('seeds/artists_table.sql')
    repo = ArtistRepository(db_connection)
    artists = repo.all()
    assert artists == [
        Artist(1, 'Pixies', 'Rock'),
        Artist(2, 'ABBA', 'Pop'),
        Artist(3, 'Taylor Swift', 'Pop'),
        Artist(4, 'Nina Simone', 'Jazz')
    ]

def test_artist_repo_add(db_connection):
    db_connection.seed('seeds/artists_table.sql')
    repo = ArtistRepository(db_connection)
    repo.add(Artist(None, 'System of a Down', 'Metal'))
    artists = repo.all()
    assert artists == [
        Artist(1, 'Pixies', 'Rock'),
        Artist(2, 'ABBA', 'Pop'),
        Artist(3, 'Taylor Swift', 'Pop'),
        Artist(4, 'Nina Simone', 'Jazz'),
        Artist(5, 'System of a Down', 'Metal')
    ]