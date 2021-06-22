#!/usr/bin/python3
from elasticsearch import Elasticsearch
from elasticsearch.helpers import scan
import csv

class EsToCsv():
    def __init__(self, index_name, csv_filename):
        self.index_name = index_name
        self.csv_filename = csv_filename
        self.es_client = Elasticsearch()
        self.csv_file = []

    def upload_json(self):
        docs = []
        for hit in scan(self.es_client, index=self.index_name, query={"query":{"match_all":{}}}, scroll= '1ms'):
            docs.append(hit["_source"]["doc"])
        self.json_to_csv(docs)

    def json_to_csv(self, docs):
        with open(self.csv_filename, mode='w') as f:
            csv_file = csv.writer(f)
            count = 0
            for data in docs:
                if count == 0:
                    header = data.keys()
                    csv_file.writerow(header)
                    count = count + 1

                csv_file.writerow(data.values())






