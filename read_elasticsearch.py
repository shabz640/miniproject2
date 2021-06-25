#!/usr/bin/python3
import sys

from elasticsearch import Elasticsearch
from elasticsearch.helpers import scan
from configparser import ConfigParser
import logging
import csv
from read_config import ReadConfig

class PreCheckException(Exception):
    pass

class IndexException(PreCheckException):
    pass

class EsToCsv():
    def __init__(self, index_name, csv_file_name, dest_log):
        config_read = ReadConfig()
        self.es_client = Elasticsearch(hosts=["localhost"])
        self.csv_file = []
        self.index_name = index_name
        try:
            if not self.es_client.indices.exists(self.index_name):
                raise IndexException
        except IndexException:
            print("Error: Index not found")
            sys.exit()


        self.csv_file_name = csv_file_name
        logging.basicConfig(filename=dest_log, level=logging.WARNING,
                            format='%(asctime)s:%(levelname)s:%(message)s')

    def upload_json(self):
        docs = []
        for hit in scan(self.es_client, index=self.index_name, query={"query":{"match_all":{}}}, scroll= '1ms'):
            docs.append(hit["_source"]["doc"])
        self.json_to_csv(docs)

    def json_to_csv(self, docs):
        with open(self.csv_file_name, mode='w') as f:
            csv_file = csv.writer(f)
            count = 0
            for data in docs:
                if count == 0:
                    header = data.keys()
                    csv_file.writerow(header)
                    count = count + 1

                csv_file.writerow(data.values())







