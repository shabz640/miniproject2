#!/usr/bin/python3
from read_elasticsearch import EsToCsv
from read_config import ReadConfig
from elasticsearch import ElasticsearchException
from exceptions import IndexException
import sys
import os

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

config = ReadConfig(config_file)


index_name = config.get_config("config", "index_name")
csv_file = config.get_config("config", "csv_filename")
dest_log = config.get_config("config", "dest_log")
host_name = config.get_config("config", "host")

es_csv = EsToCsv(index_name, csv_file, dest_log, host_name)
try:
    es_csv.index_check()
except IndexException:
    print("Error: Index not found")
    sys.exit()

try:

    if os.path.exists(csv_file):
        with open(csv_file, mode='r') as file:
            data = file.readlines()
        lastRow = data[-1].split(",")[0]
        es_csv.upload_json1(lastRow)
    else:
        es_csv.upload_json()
except ElasticsearchException as es:
    print(es)
    sys.exit()
except:
    print(sys.exc_info())
    sys.exit()