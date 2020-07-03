from clcrypto import hash_password


class User:
    def __init__(self, username="", password="", salt=""):
        self._id = -1
        self.username = username
        self._hashed_password = hash_password(password, salt)

    @property
    def id(self):
        return self._id

    @property
    def hashed_password(self):
        return self._hashed_password

    @hashed_password.setter
    def hashed_password(self, password):
        self.set_password(password)

    def set_password(self, password, salt=""):
        self._hashed_password = hash_password(password, salt)

    def safe_to_db(self, cursor):
        if self._id == -1:
            sql = """
                INSERT INTO Users (username, hashed_password)
                VALUES (%s, %s)
                RETURNING id;
            """
            values = (self.username, self._hashed_password)
            cursor.execute(sql, values)
            self._id = cursor.fetchone()[0]
            return True
        else:
            sql = """
                UPDATE Users SET username=%s, hashed_password=%s
                WHERE id = %s
            """
            values = (self.username, self._hashed_password, self._id)
            cursor.execute(sql, values)
            return True

    def load_user_by_username(self, user_name):
        pass

if __name__ == "__main__":
    u1 = User("Joe","dupa123")
    print(u1.id)
    print(u1.hashed_password)
