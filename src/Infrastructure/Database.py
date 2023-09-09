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
        if platform.system() == 'Windows':
            self.root_dir = self.root_dir + '\\src\\Data\\'
        else:
            self.root_dir = self.root_dir + '/Data/'

    def read(self, file_name):
        file_reader = open(self.root_dir + file_name, "r", encoding="utf8")
        csv_file_reader = csv.reader(file_reader)
        rows = []
        for row in csv_file_reader:
            rows.append(row)
        file_reader.close()
        return rows

    def write(self, file_name, row):
        file_reader = open(self.root_dir + file_name, "r", encoding="utf8")
        all_lines = file_reader.readlines()
        length = len(all_lines)
        print(length)
        file_writer = open(self.root_dir + file_name, "a", encoding="utf8")

        contents = ''
        

        file_writer.write(f'{length},{row[0]},{row[1]},{row[2]},{row[3]},{row[4]}\n')
        file_writer.close()

    def search(self, file_name, email):
        file_reader = open(self.root_dir + file_name, "r", encoding='utf8')
        for row in csv.reader(file_reader):
            if row[0] == email:
                return row
        file_reader.close()
        return None
