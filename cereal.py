import csv
import os

cerealFile = os.path.join(".", "Resources", "cereal.csv")

with open(cerealFile, "r") as csvFile:
    csvReader = csv.reader(csvFile)
    header = next(csvReader)
    for row in csvReader:
        if float(row[7]) > 5:
            print(f"Cereal {row[0]} contains more than 5 grams of fiber.")
    print("\n")