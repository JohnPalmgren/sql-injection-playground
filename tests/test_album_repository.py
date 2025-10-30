from lib.album_repository import AlbumRepository
from lib.album import Album

def test_all_album(db_connection):
    db_connection.seed('seeds/albums_table.sql')
    repo = AlbumRepository(db_connection)
    albums = repo.all()
    assert albums == [
        Album(1, 'Doolittle', 1989, 1),
        Album(2, 'Surfer Rosa', 1988, 1),
        Album(3, 'Waterloo', 1974, 2),
        Album(4, 'Super Trouper', 1980, 2),
        Album(5, 'Bossanova', 1990, 1),
        Album(6, 'Lover', 2019, 3),
        Album(7, 'Folklore', 2020, 3),
        Album(8, 'I Put a Spell on You', 1965, 4)
    ]

def test_find_album(db_connection):
    db_connection.seed('seeds/albums_table.sql')
    repo = AlbumRepository(db_connection)
    album = repo.find(2)
    assert album.id == 2
    assert album.title == 'Surfer Rosa'
    assert album.release_year == 1988
    assert album.artist_id == 1

def test_create_album(db_connection):
    db_connection.seed('seeds/albums_table.sql')
    repo = AlbumRepository(db_connection)
    album = Album(None, 'Post Human', 2024, 5)
    repo.add(album)
    assert repo.all() == [
        Album(1, 'Doolittle', 1989, 1),
        Album(2, 'Surfer Rosa', 1988, 1),
        Album(3, 'Waterloo', 1974, 2),
        Album(4, 'Super Trouper', 1980, 2),
        Album(5, 'Bossanova', 1990, 1),
        Album(6, 'Lover', 2019, 3),
        Album(7, 'Folklore', 2020, 3),
        Album(8, 'I Put a Spell on You', 1965, 4),
        Album(9, 'Post Human', 2024, 5)
    ]
