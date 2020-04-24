from file_handler import FileHandler


class User:
    __users = []
    __authorize_user = []

    def __init__(self):
        self.file_handle = FileHandler('user.csv')
        self.__users = self.file_handle.get_data()

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

    def add_user(self, id, **kwargs):
        try:
            for row in self.__users:
                if row['user_id'] == id:
                    return False

            answer = self.file_handle.append_to_csv('user.csv', kwargs)
            if answer:
                return True
            else:
                return False
        except Exception as e:
            print(e)
            raise
