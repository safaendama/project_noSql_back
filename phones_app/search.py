from elasticsearch_dsl import Search
from elasticsearch_dsl.connections import connections

connections.create_connection()

def search() :
    result = Search(index = 'phones')
    result = result[0:1000]
    response = result.execute()
    return response

