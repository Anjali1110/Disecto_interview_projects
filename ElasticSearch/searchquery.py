from elasticsearch import Elasticsearch
from query import basic_search, search_with_field

INDEX = 'companydatasearch'
es=Elasticsearch("http://localhost:9200")

def search(query, field):
    query_body = search_with_field(query, field)
    res = es.search(index=INDEX, body=query_body)
    print(res)
    return res

def search(query):
    query_body = basic_search(query)
    res = es.search(index=INDEX, body=query_body)
    print(res)
    return res

