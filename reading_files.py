# Python reading files (.txt, .json, .csv)

import json
import csv

file_path = "C:\\Users\\vishw\\OneDrive\\Desktop\\Vishwas\\Python\\Bro Code\\output.txtoutput.csv"

try:
    with open(file_path, "r") as file:
        # content = file.read()
        # content = json.load(file)
        content = csv.reader(file)
        for line in content:
            # print(line[0])
            print(line[1])
        print(content)

except FileNotFoundError:
    print("File not found!")

except PermissionError:
    print("You don't have the permission to read that file")