from User import User

class User_list:
    def __init__(self):
        users = User()
        self.user_data = users.read_all_user()
    def info (self) :
        return self.user_data
