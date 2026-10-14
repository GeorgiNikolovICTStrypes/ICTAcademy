from user import User

class App:
    def __init__(self):
        self._users = {}

    def add_user(self, name,password, **goals):
        if name in self._users:
            raise ValueError('User already exists!')
        self._users[name] =  User(name, password, **goals)
    
    def remove_user(self, name, password):
        if name in self._users:
            self._users.pop(name)
        else:
            raise ValueError('User does not exist!')
      
    def login(self, name, password):
        user = self._users.get(name)
        if user and user.check_password(password):
            return user
        return None

