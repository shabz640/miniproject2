import unittest
from read_elasticsearch import EsToCsv
import csv
import os

def test_read_elasticsearch():

    index_name = "data"
    csv_filename = "my_data.csv"
    if os.path.exists(csv_filename):
        os.remove(csv_filename)

    es_csv = EsToCsv(index_name, csv_filename)
    es_csv.upload_json()
    file = open(csv_filename)
    reader = csv.reader(file)
    lines = len(list(reader))
    assert lines == 289

if __name__ == '__main__':
    unittest.main()
