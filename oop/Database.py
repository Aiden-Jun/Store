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



if __name__ == "__name__":
    email = input("이메일을 입력하세요: ")
    password = input("비밀번호를 입력하세요: ")
    name = input("이름을 입력하세요: ")

    file_writer = open("users.csv", "a", encoding="utf8")
    csv_file_writer = csv.writer(file_writer)
    csv_file_writer.writerow([email, password, name])
    file_writer.close()

    file_reader = open("users.csv", "r", encoding="utf8")
    csv_file_reader = csv.reader(file_reader)
    for row in csv_file_reader:
        print(row)
    file_reader.close()
