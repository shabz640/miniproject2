#!/usr/bin/python3

with open('deliveries.csv', mode = 'r') as file:
    data = file.readlines()
lastRow = data[-1].split(",")[0]

