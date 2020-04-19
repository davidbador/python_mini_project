from file_handler import FileHandler


class User(FileHandler):

    def user_auth(self, name, password):
        file_handle.load_from_csv('C:\\Users\\DavidBador\\PycharmProjects\\python_mini_project\\user.csv')
        this_list = file_handle.data_list
        name = name.split()
        try:
            for section in this_list:
                if section['first'] == name[0] and section['last'] == name[1] and section['password'] == password:
                    return section['role']
            return False
        except Exception as e:
            print(e)
            raise


file_handle = FileHandler()
users = User()
print(users.user_auth('Matan Cohen', 'fourthFour1992'))
