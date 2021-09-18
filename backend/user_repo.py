from database import repo


class UserRepo:
    def __init__(self):
        self.db = repo("user")

    def authenticate(self, username, password):
        entry = self.db.get_entry("username", username)
        if entry != None:
            if entry["username"] == username and entry["password"] == password:
                return entry
        return False

    def read_user(self, id):
        return self.db.read(id)

    def check_user(self, new_username):
        """
        Returns true iff this user does not exist in the database already.
        """
        return not bool(self.db.get_entry("username", new_username))

    # data = json object
    # default values: {"username":"yourstring", "password":"yourstring"}
    def create_user(self, username, password):
        return self.db.create({"username": username, "password": password})

    # data = json object
    def update_info(self, id, data):
        return self.db.update(id, data)
