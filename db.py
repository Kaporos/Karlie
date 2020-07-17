from tinydb  import TinyDB, where, Query
from tinydb_serialization import Serializer,SerializationMiddleware
from datetime import datetime
class DateTimeSerializer(Serializer):
    OBJ_CLASS = datetime  # The class this serializer handles

    def encode(self, obj):
        return obj.strftime('%Y-%m-%dT%H:%M:%S')

    def decode(self, s):
        return datetime.strptime(s, '%Y-%m-%dT%H:%M:%S')

class DB():
    def __init__(self):
        serialization = SerializationMiddleware()
        serialization.register_serializer(DateTimeSerializer(), 'TinyDate')
        self.db = TinyDB('karlie.json',storage=serialization)
        self.cursor =Query()
        self.result = []

    def addView(self,json):
        self.db.insert(json)

    def getViews(self,data):
        self.result = []

        date_min_var = "date_min"
        date_max_var = "date_max"

        keys = data.keys()
        query = "self.result = self.db.search("
        qlen = len(data)
        count = 0
        for key, value in data.items():
            if (key != date_min_var and key != date_max_var):
                query += "(self.cursor.%s == '%s')" % (key, value)
            else:
                if (key == date_min_var):
                    query += "(self.cursor.date > datetime(%s,%s,%s))" % (value.year,value.month,value.day)
                if (key == date_max_var):
                    query += "(self.cursor.date < datetime(%s,%s,%s))" % (value.year,value.month,value.day)
            count += 1
            if count < qlen:
                query += " & "

        query += ')'
        exec(query)
        return self.result