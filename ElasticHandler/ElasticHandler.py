from elasticsearch import Elasticsearch
import datetime
import json

class ElasticHandler():
    def __init__(self, url="https://39eb49ae41f748febb53d209417b9092.francecentral.azure.elastic-cloud.com:443", api_key={"search-users" : "ZzV4eUNJTUJ2SWZVOVVlV0JrMGs6VFpRSkxMWnVTYXE3SE4wUXBRenpCZw==",
                                                                                                      "search-event" : "amxWNkNJTUJ6VlB1dVFMNkUyZFY6b0s2TGQwa3VTNml5WGN2WTRIWXhPQQ=="}):
        """
        Initalizes elastic connection with api keys
        @param url: the url to the elastic server
        @param api_key: a dict of the keys according to their indexes
        """
        self.url = url
        self.api_key = api_key
        self.es_dict = {}
        for k,v in api_key.items():
            self.es_dict[k] = Elasticsearch([self.url],
                    api_key=v)

    def push_data(self, index, json):
        """
        Pushes data to a specific index
        """
        try:
            self.es_dict[index].index(
             index=index,
             document=json)
            self.es_dict[index].indices.refresh(index=index)
        except KeyError:
            print("No such index exists!")

    def query_data(self, index, query):
        """
        querys the elastic index and returns all hits
        @param query: a DSL type elastic query
        """
        try:
            result = self.es_dict[index].search(index=index,
                                                query=query)
            return result['hits']['hits']
        except KeyError:
            print("No such index exists!")
