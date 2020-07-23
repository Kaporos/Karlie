from tinydb  import TinyDB, where, Query
from tinydb_serialization import Serializer,SerializationMiddleware
from datetime import datetime
from operator import eq, ge, gt, le, lt, ne, itemgetter
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
        try :
            keys = data.keys()
            if len(keys) == 0:
                return self.db.all()
            default_op = ops.get("==")
            for key in keys:
                possible_queries = data[key]
                for query in possible_queries:
                    op = default_op
                    value = query["value"]
                    #CONVERTING STRING TO SOME TYPES
                    try: 
                        value = datetime.fromisoformat(value)
                    except:
                        pass
                    try:
                        value = int(value)
                    except:
                        pass

                    if "op" in query.keys():
                        op = ops[query["op"]]

                    queries_list.append(op(where(key), value))
            start = queries_list.pop(0)
            result = start
            for x in queries_list:
                result = result & x
            return self.db.search(result)
        except:
            return []
    def global_infos(self):
        result = {}
        result["total_views"] = len(self.db)
        countries = []
        codes = {}
        countries_tmp = {}
        entries = self.db.all()
        for entry in entries:
            country = entry["country"]
            codes[country] = entry["country_code"]
            if country in countries_tmp.keys():
                countries_tmp[country] += 1
            else:
                countries_tmp[country] = 1
        for country in countries_tmp.keys():
            countries.append({"name": country,"total":countries_tmp[country],"code":codes[country]})

        result["top_country"] = max(countries_tmp.items(), key=itemgetter(1))[0]
        result["countries"] = countries
        today = datetime.now()

        #THIS MONTH
        this_month_views = self.getViews({
            "date": [
                {
                    "value": datetime(today.year,today.month,1),
                    "op": ">"
                }
            ]
        })


        #LAST MONTH
        last_month = datetime(today.year,today.month - 1,1)
        last_month_views = self.getViews({
            "date":[
                {
                    "value": last_month,
                    "op": ">"
                },
                {
                    "value": datetime(today.year,today.month,1),
                    "op": "<"
                }
            ]
        })
        result["this_month_views"] = len(this_month_views)
        result["last_month_views"] = len(last_month_views)
        return result