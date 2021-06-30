#!/usr/bin/python3
from read_elasticsearch import EsToCsv
from read_config import ReadConfig
from elasticsearch import ElasticsearchException
from exceptions import IndexException
import sys
import os

config_file = "config_file.conf"

config = ReadConfig(config_file)
index_name = config.get_config("config", "index_name")
csv_file = config.get_config("config", "csv_filename")
dest_log = config.get_config("config", "dest_log")
host_name = config.get_config("config", "host")

try:
    es_csv = EsToCsv(index_name, csv_file, dest_log, host_name)
except IndexException:
    print("Error: Index not found")
    sys.exit()

try:
    last_id = 0
    if os.path.exists(csv_file):
        for row in open(csv_file):
            last_id = last_id + 1

    es_csv.upload_json(last_id)

except ElasticsearchException as es:
    print(es)
    sys.exit()
except:
    print(sys.exc_info())
    sys.exit()




