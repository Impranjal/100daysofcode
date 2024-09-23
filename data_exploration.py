import random
import csv
with open('cereal.csv','r') as file:
    data = csv.reader(file)
    for row in data:
        print(row)