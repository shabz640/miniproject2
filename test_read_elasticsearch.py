import pytest
from read_elasticsearch import EsToCsv
import csv
import os

def test_read_elasticsearch():

    index_name = "ipl-deliveries"
    csv_filename = "deliveries.csv"
    host_name = "localhost"
    if os.path.exists(csv_filename):
        os.remove(csv_filename)

    es_csv = EsToCsv(index_name, csv_filename, dest_log='ipl.log', host_name)
    es_csv.upload_json()
    file = open(csv_filename)
    reader = csv.reader(file)
    lines = len(list(reader))
    assert lines == 179079

if __name__ == '__main__':
    pytest.main()
