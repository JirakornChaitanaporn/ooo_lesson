import csv, os

#make file into dict
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

cities = []
with open(os.path.join(__location__, 'Cities.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        cities.append(dict(r))

countries = []
with open(os.path.join(__location__, 'Countries.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        countries.append(dict(r))

class TableDB:
    def __init__(self):
        self.table_database = []
    def insert(self, table):
        self.table_database.append(table)
    def search(self, table_name):
        i = 0
        for _dict_list in self.table_database:
            for _dict in _dict_list:
                if list(_dict.keys())[0] == table_name:
                    return i
                break
            i += 1
        return -1
    
class Table:
    def __init__(self, table_name, table: list):
        self.table = table
        self.table_name = table_name
        
    def filter(self, condition):
        for item in self.table:
            if not condition(item):
                self.table.remove(item)
    
    def aggregate(self, aggregation_function, aggregation_key):
        for key, val in self.table.items():
            if key != aggregation_key:
                self.table.remove({key:val})
        return aggregation_function(self.table)
