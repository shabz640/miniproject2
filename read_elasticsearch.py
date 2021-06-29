#!/usr/bin/python3
import sys
from exceptions import IndexException
from elasticsearch import Elasticsearch
from elasticsearch.helpers import scan
import logging
import csv
from read_config import ReadConfig

class EsToCsv():
    def __init__(self, index_name, csv_filename, dest_log, host_name):
        self.es_client = Elasticsearch([host_name])
        self.csv_file = []
        self.index_name = index_name
        self.csv_file = csv_filename
        #self.dest_log = dest_log
        logging.basicConfig(filename = dest_log, level=logging.WARNING,
                            format='%(asctime)s:%(levelname)s:%(messages)s')

    def index_check(self):
        if not self.es_client.indices.exists(self.index_name):
            raise IndexException()

    def upload_json(self):
        #Creating a new index
        docs = []
        for hit in scan(self.es_client, index=self.index_name,
                        query={"query":
                                   {"match_all":{}}},
                        scroll = '1ms'):

            docs.append(hit["_source"]["doc"])
        self.json_to_csv(docs)

    def upload_json1(self,last_id):
        #Appending to an index
        docs = []
        for hit in scan(self.es_client, index=self.index_name,
                        query={"query":
                                        {"range":
                                                {"doc.id":
                                                     {"gt": last_id }}}},
                        scroll = '1ms'):

            docs.append(hit["_source"]["doc"])
        self.json_to_csv1(docs)

    def json_to_csv(self, docs):
        with open(self.csv_file, mode='w') as f:
            csv_file = csv.writer(f)
            count = 0
            for data in docs:
                if count == 0:
                    header = data.keys()
                    csv_file.writerow(header)
                    count = count + 1

                csv_file.writerow(data.values())

    def json_to_csv1(self, docs):
        with open(self.csv_file, mode='a') as f:
            csv_file = csv.writer(f)
            count = 0
            for data in docs:
                if count == 0:
                    count = count + 1

                csv_file.writerow(data.values())