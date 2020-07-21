from tinydb  import TinyDB, where, Query
from tinydb_serialization import Serializer,SerializationMiddleware
from datetime import datetime
from operator import eq, ge, gt, le, lt, ne
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
        ops = {
            "==": eq,
            "!=": ne,
            "<=": le,
            ">=": ge,
            "<": lt,
            ">": gt,
        }
        queries_list = []
        keys = data.keys()
        default_op = ops.get("==")
        for key in keys:
            possible_queries = data[key]
            for query in possible_queries:
                op = default_op
                value = query["value"]
                if "op" in query.keys():
                    op = ops[query["op"]]

                queries_list.append(op(where(key), value))
        start = queries_list.pop(0)
        result = start
        for x in queries_list:
            result = result & x
        return self.db.search(result)