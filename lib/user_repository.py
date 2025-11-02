from lib.user import User

class UserRepository():
    def __init__(self, connection):
        self.connection = connection

    def all(self):
        command = 'SELECT * FROM users'
        rows = self.connection.execute(command)
        return [User([row["id"]], row["name"], row["email"]) for row in rows]
    
    def find(self, id):
        # Insecure SQL for demonstration
        command = f'SELECT * FROM users WHERE id = {id}'
        rows = self.connection.execute(command)
        row = rows[0]
        return User(row["id"], row["name"], row["email"], row["admin"])
    
    def authenticate_user(self, user):
        # Insecure SQL for demonstration
        command = f"SELECT * FROM users WHERE (email, password) = ('{user.email}', '{user.password}')"
        rows = self.connection.execute(command)
        if len(rows) > 0:
            row = rows[0]
            return User(row["id"], row["name"], row["email"], row["admin"])
        return None