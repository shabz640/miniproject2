#!/usr/bin/python3
import sys
from exceptions import IndexException
from elasticsearch import Elasticsearch
from elasticsearch.helpers import scan
import logging
import csv

class EsToCsv():
    def __init__(self, index_name, csv_file_name, dest_log, host_name):
        self.es_client = Elasticsearch([host_name])
        self.index_name = index_name
        self.csv_file = csv_file_name
        if not self.es_client.indices.exists(self.index_name):
            raise IndexException()

        logging.basicConfig(filename=dest_log, level=logging.WARNING,
                            format='%(asctime)s:%(levelname)s:%(messages)s')

        print(self.index_name, self.csv_file)

    def upload_json(self, last_id):
        docs = []
        for hit in scan(self.es_client, index=self.index_name,
                        query={
                            "query": {"range": {
                                "doc.id": {
                                    "gt": last_id
                                }}}
                        },
                        scroll='1ms'):
            docs.append(hit["_source"]["doc"])

        self.json_to_csv(docs, last_id)


    def json_to_csv(self, docs, last_id):
        print(last_id)

        with open(self.csv_file, mode='a') as f:
            csv_file = csv.writer(f)
            count = 0
            for data in docs:

                if count == 0:
                    header = data.keys()
                    csv_file.writerow(header)
                    count = count + 1

                csv_file.writerow(data.values())
