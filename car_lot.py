from file_handler import FileHandler
from user import User
import csv


class CarLot:
    __list_of_vehicles = []

    def __init__(self):
        self.__list_of_vehicles = []
        self.file_handle = FileHandler('user.csv')
        self.user = User()
        self.__users = self.file_handle.get_data()

    def update_salary_by_name(self, employee_salary, name):
        try:
            password_enter = input('Please enter password: ')
            is_admin = self.user.user_auth(name, password_enter)
            if is_admin == 'admin':
                enter_name = input('Please enter the name you want to update: ')
                new_name = enter_name.split()
                for row in self.__users:
                    if row['first'] == new_name[0] and row['last'] == new_name[1] and row['role'] == 'employee':
                        row['salary'] = employee_salary
                        add_employee = self.file_handle.update_csv("user.csv", row['user_id'], row)
                        if add_employee:
                            return True
                        else:
                            return False
                return False
            else:
                return False
        except Exception as e:
            print(e)
            raise

    @staticmethod
    def add_to_fleet(external_csv_fleet_file):
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

            if next(external_file) == next(internal_file):
                with open('vehicle.csv', 'a') as csv_append:
                    for row in external_file:
                        csv_append.writelines(row)
                return True
            else:
                return False
        except Exception as e:
            print(e)
            raise

    def get_fleet_size(self):
        try:
            with open('vehicle.csv', "r") as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=",")
                next(csv_file)
                for row in csv_reader:
                    self.__list_of_vehicles.append(row)
                return len(self.__list_of_vehicles)
        except Exception as e:
            print(e)
            raise

    @staticmethod
    def get_all_cars_by_brand(brand):
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
