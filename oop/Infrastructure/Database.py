import csv


class Database(object):
    __instance = None

    def __new__(cls, *args, **kwargs):
        print(cls.__instance)
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            print("데이터베이스 객체가 만들어 졌다!")
            print(cls.__instance)
        return cls.__instance

    def read_from_file(self, file_name):
        file_reader = open(file_name, "r", encoding="utf8")
        csv_file_reader = csv.reader(file_reader)

        rows = []
        for row in csv_file_reader:
            rows.append(row)
        file_reader.close()

        return rows

    def write_file(self, file_name, content):
        pass

    def get_user(self, file_name, email):
        file_reader = open(file_name, "r", encoding="utf8")
        csv_file_reader = csv.reader(file_reader)
        for row in csv_file_reader:
            if row[0] == email:
                file_reader.close()
                return row
        file_reader.close()
        return None

    def add_user_row(self, email, password, name, type):
        file_writer = open("../users.csv", "a", encoding="utf8")
        csv_file_writer = csv.writer(file_writer)
        csv_file_writer.writerow([email, password, name, type])
        file_writer.close()

    def check_email_existence(self, email):
        file_reader = open("../users.csv", "r", encoding="utf8")
        csv_file_reader = csv.reader(file_reader)
        for row in csv_file_reader:
            if row[0] == email:
                return True
        file_reader.close()
        return False
