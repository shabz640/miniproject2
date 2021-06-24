#!/usr/bin/python3
import logging
from  read_config import ReadConfig
import shutil
from elasticsearch import Elasticsearch

try:
    es_client = Elasticsearch()
except Exception as e:
    if "Connection redused in err.message":
        logging.error("Elasticsearch not accessible")

class PreCheckException():
    def __init__(self):
        pass

config_file = "variables1.conf"
read_file = ReadConfig()
my_list = read_file.read_config(config_file)

index_name = my_list[0]
csv_file = my_list[1]
dest_log = my_list[2]

total, used, free = shutil.disk_usage("/")
free_space = free/ (2 ** 30)

def pre_check():
    if not os.path.exists(config_file):
        raise PreCheckException("Config File Not Found")

    elif not es_client.indices.exists(index=index_name):
        raise PreCheckException("ElasticsearchIndex in config file doesn't exist")
    else free_space < 1:
        raise PreCheckException("Not enough space in the Disk")

try:
    pre_check()
except PreCheckException as e:
    print(e)





