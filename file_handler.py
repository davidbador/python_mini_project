import csv
from logger import Logger


class FileHandler(Logger):

    def load_from_csv(self, file_name):
        try:
            self.data_list = []
            with open(file_name, 'r') as csv_file:
                read_this = csv.DictReader(csv_file)
                for i in read_this:
                    self.data_list.append(i)
        except IOError as e:
            print(FileExistsError(e))
            raise

    def append_to_csv(self, file_name, data):
        with open(file_name, 'r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=",")
            for column in csv_reader:
                if data["user_id"] == column[0]:
                    return False
        with open(file_name, 'a+') as csv_file:
            try:
                csv_writer = csv.writer(csv_file, delimiter=",")
                csv_writer.writerow([data['user_id'], data['first'], data['last'], data['password'],
                                    data['position'], data['salary'], data['role']])
                self.add_to_log('{} {} with id {} was created at this date and time\n'.format(data['first'],
                                                                                              data['last'],
                                                                                              data['user_id']))
                return True
            except Exception as e:
                print(e)
                raise


file_handle = FileHandler()

data_of_person = {
    "user_id": "1000000001",
    "first": "Rommi",
    "last": "Englard",
    "password": "tenthTen1992",
    "position": "Head of SQL",
    "salary": "100000",
    "role": "admin",
}

print(file_handle.append_to_csv('C:\\Users\\DavidBador\\PycharmProjects\\python_mini_project\\user.csv',
                                data_of_person))
