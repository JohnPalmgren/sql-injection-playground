
# def test_get_artists(web_client, db_connection):
#     db_connection.seed('seeds/artists_table.sql')
#     res = web_client.get('/artists')
#     assert res.status_code == 200
#     artists = res.data.decode('utf-8')
#     assert artists == "Artist(1, Pixies, Rock)\nArtist(2, ABBA, Pop)\nArtist(3, Taylor Swift, Pop)\nArtist(4, Nina Simone, Jazz)"

# def test_post_artist(web_client, db_connection):
#     db_connection.seed('seeds/artists_table.sql')
#     post_res = web_client.post('/artists', data={"name":"System of a Down", "genre": "Metal"})
#     assert post_res.status_code == 200
#     get_res = web_client.get('/artists')
#     artists = get_res.data.decode('utf-8')
#     assert artists == "Artist(1, Pixies, Rock)\nArtist(2, ABBA, Pop)\nArtist(3, Taylor Swift, Pop)\nArtist(4, Nina Simone, Jazz)\nArtist(5, System of a Down, Metal)"



