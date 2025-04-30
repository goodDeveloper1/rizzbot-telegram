import csv
import json

with open("raw_dataset.csv", "r") as file:
    reader = csv.reader(file)
    fiel = []
    for row in reader:
        fiel.append(row[0])
    
    with open("dataset.json", "w") as o_file:
        json.dump(fiel, o_file, indent=4)