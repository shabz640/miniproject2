#!/usr/bin/python3
from read_elasticsearch import EsToCsv
from  read_config import ReadConfig


read_file = ReadConfig()
my_list = read_file.read_config("variables.conf")

index_name = my_list[0]
csv_file = my_list[1]
dest_log = my_list[2]

es_csv = EsToCsv(index_name, csv_file, dest_log)
es_csv.upload_json()


