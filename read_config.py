#!/usr/bin/python3
from configparser import ConfigParser

class ReadConfig():
    def __init__(self):
        pass

    def read_config(self,config_file):
        parser = ConfigParser()
        parser.read(config_file)
        index_name = parser.get("config", "index_name")
        csv_filename = parser.get("config", "csv_filename")
        dest_log = parser.get("config", "dest_log")
        return index_name,csv_filename,dest_log


