from file_handler import FileHandler
import datetime

class Vehicle:

    def __init__(self):
        self.file_handle = FileHandler('vehicle.csv')
        self.__data_list = self.file_handle.get_data()

    def update_vehicle_by_id(self, id, **kwargs):
        try:
            self.file_handle.load_from_csv('vehicle.csv')
            self.file_handle.remove_from_csv('vehicle.csv', id)
            answer = self.file_handle.append_to_csv('vehicle.csv', kwargs)
            if answer:
                return True
            else:
                return False
        except Exception as e:
            print(e)
            raise

    def get_time_to_test(self, id):
        self.file_handle.load_from_csv('vehicle.csv')
        time = datetime.datetime.now()
        current_year = time.strftime("%Y")
        try:
            for row in self.__data_list:
                id = str(id)
                if row['user_id'] == id:
                    next_test = int(current_year) - int(row['Last_Test'])
                    if next_test >= 2:
                        return 'Vehicle with user id ' + id + ' must be tested right away!'
                    elif next_test == 1 or next_test == 0:
                        if next_test == 1:
                            return 'Vehicle with user id ' + id + ' has 1 year until its next test.'
                        elif next_test == 0:
                            return 'Vehicle with user id ' + id + ' has 2 years until its next test.'
                    elif next_test < 0:
                        return False
            return False
        except Exception as e:
            print(e)
            raise
