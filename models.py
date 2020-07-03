
class User:
    def __init__(self, username, _hashed_password, _id=-1):
        self.username = username
        self.__id = _id
        self.__hashed_password = _hashed_password

    @property
    def _id(self):
        return self.__id
    @property
    def _hashed_password(self):
        return self.__hashed_password

    @_hashed_password.setter
    def _hashed_password(self, new_password):
        self.__hashed_password = new_password

    def load_user_by_username(self, user_name):




u1 = User("Arek","AAA", 1)
print(u1._id)

u1._hashed_password="elo"
print(u1._hashed_password)