import csv
from logger import Logger


class FileHandler:

    def __init__(self):
        self.data_list = []
        self.log_it = Logger()

    def load_from_csv(self, file_name):
        try:
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
                self.log_it.add_to_log('{} {} with id {} was created at this date and time\n'.format(data['first'],
                                                                                                     data['last'],
                                                                                                     data['user_id']))
                return True
            except Exception as e:
                print(e)
                raise

    def remove_from_csv(self, csv_file_name, id):
        try:
            lines = list()
            answer = False
            with open(csv_file_name, 'r') as read_file:
                csv_reader = csv.reader(read_file)
                for row in csv_reader:
                    if row[0] != id:
                        lines.append(row)
                    else:
                        answer = True
            with open(csv_file_name, 'w', newline='') as write_file:
                csv_writer = csv.writer(write_file)
                csv_writer.writerows(lines)
                return answer
        except Exception as e:
            print(e)
            raise

    def update_csv(self, csv_file_name, id, row):
        file_handle = FileHandler()
        answer = file_handle.remove_from_csv(csv_file_name, id)
        try:
            if answer:
                append_this = file_handle.append_to_csv(csv_file_name, row)
                if append_this:
                    return True
                else:
                    return False
            else:
                return False
        except Exception as e:
            print(e)
            raise
