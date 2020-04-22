import datetime
import os


class Logger:

    @staticmethod
    def add_to_log(msg):
        date_set_up = datetime.datetime.now()
        date = date_set_up.strftime("%d/%m/%Y %H:%M:%S")
        hour = date_set_up.strftime("%H")
        log_file = "logs\\my_app-" + hour + ".log"
        for file in os.listdir('logs'):
            while len(os.listdir('logs')) > 24:
                os.listdir('logs').remove(file[0])
        if log_file not in os.listdir('logs'):
            with open(log_file, "w") as csv_file:
                csv_file.write(date + " - " + msg)
        else:
            with open(log_file, "a") as csv_file:
                csv_file.write(date + " - " + msg)
