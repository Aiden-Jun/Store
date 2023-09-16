from src.Infrastructure.Database import Database


class BaseRepository(object):
    def __init__(self, file_name):
        self._file_name = file_name
        self._db = Database()

    def save(self, domain):
        row = []
        for k, v in domain.__dict__.items():
            row.append(v)
        self._db.update(self._file_name, row)


if __name__ == "__main__":
    pass
