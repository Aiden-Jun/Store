import csv
import os


class Database(object):
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self):
        self.root_dir = os.getcwd() + '/Data/'

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
        csv_file_writer = csv.writer(file_writer)
        csv_file_writer.writerows(rows)
        file_writer.close()

    def search(self):
        pass
