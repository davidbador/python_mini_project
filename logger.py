import datetime
import os
from logging import handlers


class Logger:

    def add_to_log(self, msg):
        date_set_up = datetime.datetime.now()
        hour_word = date_set_up.strftime("%H")
        date = date_set_up.strftime("%d/%m/%Y %H:%M:%S")
        for file in os.listdir('logs'):
            while len(os.listdir('logs')) > 24:
                os.listdir('logs').remove(file[0])
        file_path = "log_"+hour_word+".csv"
        if file_path not in os.listdir('logs'):
            with open("logs\\"+file_path, "w") as csv_file:
                csv_file.write(date + " - " + msg)
        else:
            with open("logs\\"+file_path, "a") as csv_file:
                csv_file.write(date + " - " + msg)
