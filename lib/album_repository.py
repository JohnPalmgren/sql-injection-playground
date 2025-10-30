from lib.album import Album

class AlbumRepository():
    def __init__(self, connection):
        self.connection = connection

    def all(self):
        command = 'SELECT * FROM albums'
        rows = self.connection.execute(command)
        albums = []
        for row in rows:
            albums.append(Album(row["id"], row["title"], row["release_year"], row["artist_id"]))
        return albums

    def find(self, id):
        command = 'SELECT * FROM albums WHERE id = %s'
        rows = self.connection.execute(command, [id])
        album = rows[0]
        return Album(album["id"], album["title"], album["release_year"], album["artist_id"])
    
    def add(self, album):
        command = 'INSERT INTO albums (title, release_year, artist_id) VALUES (%s, %s, %s)'
        self.connection.execute(command, [album.title, album.release_year, album.artist_id])