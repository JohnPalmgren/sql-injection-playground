from lib.artist import Artist

class ArtistRepository():
    def __init__(self, connection):
        self.connection = connection

    def all(self):
        command = 'SELECT * FROM artists'
        rows =self.connection.execute(command)
        return [Artist(row["id"], row["name"], row["genre"]) for row in rows]

    def add(self, artist):
        command = 'INSERT INTO artists (name, genre) VALUES (%s, %s)'
        self.connection.execute(command, [artist.name, artist.genre])
