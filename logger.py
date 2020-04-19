import datetime


class Logger:

    def add_to_log(self, msg):
        with open("C:\\Users\\DavidBador\\PycharmProjects\\python_mini_project\\user.csv", "a") as csv_file:
            date_set_up = datetime.datetime.now()
            date = date_set_up.strftime("%d/%m/%Y %H:%M:%S")
            csv_file.write(date + " - " + msg)
