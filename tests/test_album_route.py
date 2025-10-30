from lib.album import Album

# def test_post_albums(web_client, db_connection):
#     db_connection.seed('seeds/albums_table.sql')
#     post_response = web_client.post('/albums', data={'title': 'Post Human', 'release_year': '2024', 'artist_id':'5'})
#     assert post_response.status_code == 200
#     get_response = web_client.get('albums')
#     albums = get_response.data.decode('utf-8')
#     assert albums == 'Album(1, Doolittle, 1989, 1)\nAlbum(2, Surfer Rosa, 1988, 1)\nAlbum(3, Waterloo, 1974, 2)\nAlbum(4, Super Trouper, 1980, 2)\nAlbum(5, Bossanova, 1990, 1)\nAlbum(6, Lover, 2019, 3)\nAlbum(7, Folklore, 2020, 3)\nAlbum(8, I Put a Spell on You, 1965, 4)\nAlbum(9, Post Human, 2024, 5)'


# def test_get_albums(web_client, db_connection):
#     db_connection.seed('seeds/albums_table.sql')
#     res = web_client.get('/albums')
#     assert res.status_code == 200
#     albums = res.data.decode('utf-8')
#     assert albums == 'Album(1, Doolittle, 1989, 1)\nAlbum(2, Surfer Rosa, 1988, 1)\nAlbum(3, Waterloo, 1974, 2)\nAlbum(4, Super Trouper, 1980, 2)\nAlbum(5, Bossanova, 1990, 1)\nAlbum(6, Lover, 2019, 3)\nAlbum(7, Folklore, 2020, 3)\nAlbum(8, I Put a Spell on You, 1965, 4)'
