import csv


class Database(object):
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
        file_writer = open("users.csv", "a", encoding="utf8")
        csv_file_writer = csv.writer(file_writer)
        csv_file_writer.writerow([email, password, name, type])
        file_writer.close()

    def check_email_existence(self, email):
        file_reader = open("users.csv", "r", encoding="utf8")
        csv_file_reader = csv.reader(file_reader)
        for row in csv_file_reader:
            if row[0] == email:
                return True
        file_reader.close()
        return False