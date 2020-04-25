from file_handler import FileHandler
from user import User
import csv


class CarLot:
    __list_of_vehicles = []
    __employee_cars = []
    __filter_list = []
    __vehicle_data_list = []

    def __init__(self):
        self.__list_of_vehicles = []
        self.__filter_list = []
        self.__employee_cars = []
        self.file_handle = FileHandler('user.csv')
        self.file_handle_vehicle = FileHandler('vehicle.csv')
        self.user = User()
        self.__data_list = self.file_handle.get_data()
        self.__vehicle_data_list = self.file_handle_vehicle.get_data()

    def update_salary_by_name(self, employee_salary, name):
        try:
            password_enter = input('Please enter password: ')
            is_admin = self.user.user_auth(name, password_enter)
            if is_admin == 'admin':
                enter_name = input('Please enter the name you want to update: ')
                new_name = enter_name.split()
                for row in self.__data_list:
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

    def get_all_cars_by_filter(self, and_or="AND", **kwargs):
        answer = False
        try:
            with open('vehicle.csv', 'r') as csv_file:
                read_this = csv.DictReader(csv_file, delimiter=",")
                for i in read_this:
                    self.__filter_list.append(i)
            print_rows = []
            for row in self.__filter_list:
                if and_or == "AND":
                    if all(row.get(key, None) == val for key, val in kwargs.items()):
                        print_rows.append(row)
                        answer = True
                elif and_or == "OR":
                    if any(row.get(key, None) == val for key, val in kwargs.items()):
                        print_rows.append(row)
                        answer = True
            if answer:
                print(print_rows)
                return answer
            return answer
        except Exception as e:
            print(e)
            raise

    def how_many_own_more_than_one_car(self):
        try:
            with open('vehicle.csv', 'r') as csv_file:
                read_this = csv.DictReader(csv_file, delimiter=",")
                for i in read_this:
                    self.__filter_list.append(i)
            result = {}
            for key in self.__filter_list:
                if 'Owner' in key:
                    result[key['Owner']] = result.get(key['Owner'], 0) + 1
            return [owner for owner, cars in result.items() if cars > 1]
        except Exception as e:
            print(e)
            raise

    def does_employee_have_car(self):
        try:
            for row in self.__data_list:
                for vehicle in self.__vehicle_data_list:
                    name = row['first'] + ' ' + row['last']
                    if name == vehicle['Owner'] and (row['role'] == 'admin' or row['role'] == 'employee'):
                        self.__employee_cars.append(row)
                        if row in self.__employee_cars:
                            break
            if len(self.__employee_cars) > 0:
                return self.__employee_cars
            else:
                return False
        except Exception as e:
            print(e)
            raise
