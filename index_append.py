#!/usr/bin/python3
from read_elasticsearch import EsToCsv
from read_config import ReadConfig
from elasticsearch import ElasticsearchException
from elasticsearch import Elasticsearch
import sys

es_client = Elasticsearch(hosts=(["localhost"]))
read_file = ReadConfig()

config_file = "config_file.conf"

try:
    f = open(config_file)
    f.close()
except FileNotFoundError:
    print("Config File Doesn't exist")
    sys.exit()
except:
    print("Unexpected Error:", sys.exc_info())
    sys.exit()




my_list = read_file.read_config(config_file)
index_name = my_list[0]
csv_file = my_list[1]
dest_log = my_list[2]

with open(csv_file, mode ='r') as file:
    data = file.readlines()
lastRow = data[-1].split(",")[0]

try:
    es_csv = EsToCsv(index_name, csv_file, dest_log)
    es_csv.upload_json1(lastRow)
except ElasticsearchException as es:
    print(es)
    sys.exit()
except:
    print("Unexpected Error:", sys.exc_info())
    sys.exit()
