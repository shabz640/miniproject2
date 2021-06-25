#!/usr/bin/python3
from read_elasticsearch import EsToCsv
from read_config import ReadConfig
from elasticsearch import ElasticsearchException
from elasticsearch import Elasticsearch
import sys

class PreCheckException(Exception):
    pass

class IndexException(PreCheckException):
    pass

es_client = Elasticsearch(hosts=(["localhost"]))

config_file = "config_file.conf"

try:
    f = open(config_file)
    f.close()
except FileNotFoundError:
    print("Config File Doesn't exist")
    sys.exit()
except:
    print("Some other File related Error")

read_file = ReadConfig()

my_list = read_file.read_config(config_file)
index_name = my_list[0]
csv_file = my_list[1]
dest_log = my_list[2]

try:
    es_csv = EsToCsv(index_name, csv_file, dest_log)
    es_csv.upload_json()
except ElasticsearchException as es:
    print(es)
    sys.exit()