from elasticsearch import Elasticsearch, helpers
from elasticsearch_dsl import Index
import json, re
import codecs
import unicodedata

es = Elasticsearch("http://localhost:9200")
INDEX = 'companydatasearch'
# es.indices.delete(index="companydatasearch", ignore=[400,404])
# print(es.cat.indices())

# Creating index if not manually created
def createIndex():
    index = Index(INDEX, using=es)
    res = index.create()
    print(res)

def read_all_data():
    with open('sample_data-240k-1.json', 'r', encoding='utf-8-sig') as f:
        all_data = json.loads(f.read())
        res_list = [i for n, i in enumerate(all_data['results']) ]
        return res_list

def genData(data_array):
    for data in data_array:
        Name = data.get("Name", None)
        Address = data.get("Address",None)
        Date = data.get("Date", None)
        Number = data.get("Number", None)
        Circle = data.get("Circle", None)
        Operator = data.get("Operator", None)

        yield {
            "_index": "companydatasearch",
            "_source": {
                "Name": Name,
                "Address": Address,
                "Date": Date,
                "Number": Number,
                "Circle": Circle,
                "Operator": Operator
            },
        }

createIndex()
all_data = read_all_data()
helpers.bulk(es,genData(all_data))