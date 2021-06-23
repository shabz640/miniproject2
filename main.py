#!/usr/bin/python3
from read_elasticsearch import EsToCsv
import logging, os
from configparser import ConfigParser

parser = ConfigParser()
parser.read("variables.conf")
index_name = parser.get("config", "index_name")
csv_filename = parser.get("config", "csv_filename")
dest_log = parser.get("config", "dest_log")

logging.basicConfig(filename= dest_log, level=logging.WARNING,
                    format='%(asctime)s:%(levelname)s:%(message)s')

es_csv = EsToCsv(index_name, csv_filename)
es_csv.upload_json()
