from file_handler import FileHandler


class Vehicle:

    def __init__(self):
        self.file_handle = FileHandler('vehicle.csv')

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
