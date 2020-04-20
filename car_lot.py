import csv
from file_handler import FileHandler


class CarLot:

    def update_salary_by_name(self, employee_salary, name):
        name = name.split()
        with open("user.csv", "r") as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                if row[1] == name[0] and row[2] == name[1] and row[6] == "admin":
                    answer = file_handle.update_csv("user.csv", )


file_handle = FileHandler()
