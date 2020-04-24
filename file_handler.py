import csv
from logger import Logger
import operator


class FileHandler:
    __data_list = []
    __key_list = []

    def __init__(self, file_name):
        self.__data_list = []
        self.__key_list = []
        self.log_it = Logger()
        self.load_from_csv(file_name)

    def load_from_csv(self, file_name):
        try:
            with open(file_name, 'r') as csv_file:
                read_this = csv.DictReader(csv_file)
                for i in read_this:
                    self.__data_list.append(i)
        except IOError as e:
            print(FileExistsError(e))
            raise

    def get_data(self):
        return self.__data_list

    def append_to_csv(self, file_name, data):
        with open(file_name, 'r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=",")
            for column in csv_reader:
                if data == column:
                    return False
        csv_reader = open(file_name, 'r')
        with open(file_name, 'a+') as csv_file:
            try:
                csv_writer = csv.writer(csv_file, delimiter=",")
                csv_list = next(csv_reader).replace('\n', '')
                new_list = csv_list.split(",")
                if new_list != list(data.keys()):
                    return False
                csv_writer.writerow(data.values())
                self.log_it.add_to_log('This user was created at this date and time\n')
                return True
            except Exception as e:
                print(e)
                raise

    @staticmethod
    def remove_from_csv(csv_file_name, id):
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
        self.load_from_csv('user.csv')
        answer = self.remove_from_csv(csv_file_name, id)
        try:
            if answer:
                append_this = self.append_to_csv(csv_file_name, row)
                if append_this:
                    return True
                else:
                    return False
            else:
                return False
        except Exception as e:
            print(e)
            raise

    def sort_by_key(self, file_name, key, direction):
        try:
            with open('user.csv', 'r') as csv_file:
                csv_reader = csv.DictReader(csv_file)

                if direction == "normal":
                    arrange = sorted(csv_reader, key=operator.itemgetter(key), reverse=False)
                elif direction == 'reverse':
                    arrange = sorted(csv_reader, key=operator.itemgetter(key), reverse=True)
                else:
                    return False

                for section in arrange:
                    self.__key_list.append(section)

            with open(file_name, 'w', newline="") as new_file:
                keys = self.__key_list[0].keys()
                csv_writer = csv.DictWriter(new_file, keys)
                csv_writer.writeheader()
                csv_writer.writerows(self.__key_list)
                return True

        except Exception as e:
            print(e)
            raise
