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

    def append(self, file_name, row):
        file_reader = open(self.root_dir + file_name, "r", encoding="utf8")
        all_lines = file_reader.readlines()
        length = len(all_lines)
        file_reader.close()

        file_writer = open(self.root_dir + file_name, "a", encoding="utf8")
        content = str(length)
        for i in range(len(row)):
            content += f',{row[i]}'
        content += '\n'
        file_writer.write(content)
        file_writer.close()

    def update(self, file_name, new_row):
        file_reader = open(self.root_dir + file_name, "r", encoding="utf8")
        csv_file_reader = csv.reader(file_reader)
        rows = []
        for row in csv_file_reader:
            print(row, new_row)
            if row[0] == new_row[0]:
                rows.append(new_row)
            else:
                rows.append(row)
        file_reader.close()

        file_writer = open(self.root_dir + file_name, "w", encoding="utf8")
        csv_file_writer = csv.writer(file_writer)
        csv_file_writer.writerows(rows)
        file_writer.close()
