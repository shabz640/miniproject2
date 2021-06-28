#!/usr/bin/python3
from configparser import ConfigParser

class ReadConfig():
    def __init__(self, config_file):
        parser = ConfigParser()
        parser.read(config_file)
        self.parser = parser


    def get_config(self, sections, keys):
        return self.parser.get(sections, keys)

