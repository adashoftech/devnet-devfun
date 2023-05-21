import csv
from pprint import pprint

# samplefile = open('NetworkInventory.csv')
# samplereader = csv.reader(samplefile)
# sampledata = list(samplereader)

# pprint(sampledata)

with open("NetworkInventory.csv") as data:
    csv_list = csv.reader(data)
    next(csv_list, None)
    for row in csv_list:
        device = row[0]
        location = row[3]
        ip = row[5]
        print(f"{device} is in {location.rstrip()} and has IP {ip}.")