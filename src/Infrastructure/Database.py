import csv
import os

# __init__ function doesn't work on my computer because my computer does not use / instead \
# So if mac, / if windows, \
import platform

class Database(object):
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self):
            self.root_dir = os.getcwd()
            self.root_dir = self.root_dir + '\\src\\Data\\'

    def read(self, file_name):
        file_reader = open(self.root_dir + file_name, "r", encoding="utf8")
        csv_file_reader = csv.reader(file_reader)
        rows = []
        for row in csv_file_reader:
            rows.append(row)
        file_reader.close()
        return rows

    def write(self, file_name, rows):
        file_writer = open(self.root_dir + file_name, "a", encoding="utf8")
        file_writer.write(f'{rows[0]},{rows[1]},{rows[2]},{rows[3]}\n')
        file_writer.close()

    def search(self, file_name, email):
        file_reader = open(self.root_dir + file_name, "r", encoding='utf8')
        for row in csv.reader(file_reader):
            if row[0] == email:
                return row
        file_reader.close()
        return None