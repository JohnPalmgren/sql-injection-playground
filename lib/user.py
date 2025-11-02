class User():
    def __init__(self, id, name, email, admin=False, password=None):
        self.id = id
        self.name = name
        self.email = email
        self.admin = admin
        self.password = password