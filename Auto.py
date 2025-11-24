from Auto_Database import Database as DB

#class definition Auto extends Database
class Auto(DB.Database):
    #constructor           class eigenschaften
    def __init__(self, name="", brand="", sql_query =""):

        self.name = name
        self.brand = brand
        self.sql_query = sql_query
        super().__init__(self.sql_query)
        if not self.name.__len__():
            self.name = "name is not set" 
        if not self.brand.__len__():
            self.brand = "brand is not set" 
    def show(self):
        print(self.name)
        print(self.brand)

#import Auto in einer anderen Datei
