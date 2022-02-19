from ast import Pass


class Database:
    # 아래에 코드를 작성해 주세요.
    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.db = {}

    def insert(self, field, value):
        # 아래에 코드를 작성해 주세요.
        if len(self.db.values()) < self.size:
            self.db[field] = value
        else:
            Pass

    def select(self, field):
        if field in self.db:
            return self.db[field]
        else:
            return None

    def update(self, field, value):
        if field in self.db:
            self.db[field] = value

    def delete(self, field):
        if field in self.db:
            del self.db[field]

