
# Elastic Search To csv

Read from elastic search index and write to a csv

  
## How to install

To deploy this project run

./main.py

If we have to append to the csv from middle of the index in case of any indexing failure run

./index_append.py	

  
## Prerequisites

pip install -r requirements.txt


    
## Running Tests

To run tests, run the following command


##Below test will read from ipl-deliveries and see if all lines are wrote to deliveries.csv

pytest test_read_elasticsearch.py

  
