import pandas as pd
""" import csv

with open("master.csv", "r", newline='') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row[]) """

data = pd.read_csv('master.csv')

print(data.info())
