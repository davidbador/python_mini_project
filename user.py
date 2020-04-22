from file_handler import FileHandler


class User:
    __users = []
    __authorize_user = []

    def __init__(self):
        file_handle = FileHandler('user.csv')
        self.__users = file_handle.get_data()

    def user_auth(self, name, password):
        name = name.split()
        try:
            for section in self.__users:
                if section['first'] == name[0] and section['last'] == name[1] and section['password'] == password:
                    return section['role']
            return False
        except Exception as e:
            print(e)
            raise
