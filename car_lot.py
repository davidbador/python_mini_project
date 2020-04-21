from file_handler import FileHandler
from user import User


class CarLot:

    def __init__(self):
        self.file_handle = FileHandler()
        self.use = User()

    def update_salary_by_name(self, employee_salary, name):
        try:
            password_enter = input('Please enter password: ')
            is_admin = self.use.user_auth(name, password_enter)
            if is_admin == 'admin':
                self.file_handle.load_from_csv('user.csv')
                this_list = self.file_handle.data_list
                enter_name = input('Please enter the name you want to update: ')
                new_name = enter_name.split()
                for row in this_list:
                    if row['first'] == new_name[0] and row['last'] == new_name[1]:
                        if row['role'] == 'employee':
                            row['salary'] = employee_salary
                            remove_employee = self.file_handle.remove_from_csv("user.csv", row['user_id'])
                            if remove_employee:
                                add_employee = self.file_handle.append_to_csv("user.csv", row)
                                if add_employee:
                                    return True
                                else:
                                    return False
                            else:
                                return False
                        else:
                            return False
                else:
                    return False
        except Exception as e:
            print(e)
            raise
