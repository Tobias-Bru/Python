class Database():
    def __init__(self, sql_query=""):
        self.sql_query = sql_query
        if not self.sql_query.__len__():
            print("sql_query is not set")

    def __connect(self):
        print("i am private function and i try to connect DB")

    def insert(self):
        self.__connect()
        print(f"i will give {self.sql_query} to DB")

    def update(self):
        self.__connect()
        print(f"i will give {self.sql_query} to DB")

    def delete(self):
        self.__connect()
        print(f"i will give {self.sql_query} to DB")

    def select(self):
        self.__connect()
        print(f"i will give {self.sql_query} to DB")