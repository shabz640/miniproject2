#!/usr/bin/python3
from elasticsearch import Elasticsearch
from elasticsearch.helpers import scan
from configparser import ConfigParser
import logging
import csv

class EsToCsv():
    def __init__(self):
        parser = ConfigParser()
        parser.read("variables.conf")
        self.index_name = parser.get("config", "index_name")
        self.csv_filename = parser.get("config", "csv_filename")
        dest_log = parser.get("config", "dest_log")
        self.es_client = Elasticsearch()
        self.csv_file = []
        logging.basicConfig(filename=dest_log, level=logging.WARNING,
                            format='%(asctime)s:%(levelname)s:%(message)s')

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





