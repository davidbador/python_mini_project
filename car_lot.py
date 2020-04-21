from file_handler import FileHandler
from user import User
import csv


class CarLot:

    def __init__(self):
        self.list_of_vehicles = []
        self.user = User()

    def update_salary_by_name(self, employee_salary, name):
        try:
            password_enter = input('Please enter password: ')
            is_admin = self.user.user_auth(name, password_enter)
            if is_admin == 'admin':
                file_handle = FileHandler()
                file_handle.load_from_csv('user.csv')
                this_list = file_handle.data_list
                enter_name = input('Please enter the name you want to update: ')
                new_name = enter_name.split()
                for row in this_list:
                    if row['first'] == new_name[0] and row['last'] == new_name[1] and row['role'] == 'employee':
                        row['salary'] = employee_salary
                        file_handle.remove_from_csv("user.csv", row['user_id'])
                        add_employee = file_handle.append_to_csv("user.csv", row)
                        if add_employee:
                            return True
                        else:
                            return False
                    else:
                        return False
            else:
                return False
        except Exception as e:
            print(e)
            raise

    def add_to_fleet(self, external_csv_fleet_file):
        try:
            with open(external_csv_fleet_file, "r") as csv_external:
                csv_reader = csv.reader(csv_external)
                external_headers = next(csv_reader)
            with open("vehicle.csv", "r") as csv_file:
                csv_reader = csv.reader(csv_file)
                internal_headers = next(csv_reader)
            if external_headers != internal_headers:
                return False

            external_file = open(external_csv_fleet_file, "r")

            internal_file = open("vehicle.csv", "r")

            if external_file != internal_file:
                with open('vehicle.csv', 'a') as csv_append:
                    next(external_file)
                    for row in external_file:
                        csv_append.writelines(row)
                return True
        except Exception as e:
            print(e)
            raise

    def get_fleet_size(self):
        try:
            with open('vehicle.csv', "r") as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=",")
                next(csv_file)
                for row in csv_reader:
                    self.list_of_vehicles.append(row)
                return len(self.list_of_vehicles)
        except Exception as e:
            print(e)
            raise

    def get_all_cars_by_brand(self, brand):
        try:
            brand_list = []
            with open('vehicle.csv', "r") as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=",")
                for row in csv_reader:
                    if row[0] == brand:
                        brand_list.append(row)
                return len(brand_list)
        except Exception as e:
            print(e)
            raise
