from lib.artist import Artist

class ArtistRepository():
    def __init__(self, connection):
        self.connection = connection

    def all(self):
        command = 'SELECT * FROM artists'
        rows =self.connection.execute(command)
        return [Artist(row["id"], row["name"], row["genre"]) for row in rows]

    def add(self, artist):
        command = 'INSERT INTO artists (name, genre) VALUES (%s, %s) RETURNING id'
        rows = self.connection.execute(command, [artist.name, artist.genre])
        row= rows[0]
        artist.id = row["id"]
        return artist
    
    def find(self, id):
        command = 'SELECT * FROM artists WHERE id = %s'
        rows = self.connection.execute(command, [id])
        row = rows[0]
        return Artist(row["id"], row["name"], row["genre"])