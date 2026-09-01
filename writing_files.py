# Python writing files (.txt, .json, .csv)

import csv
import json

employees = [["Name", "Age", "Job"], 
             ["Vishwas", 19, "Manager"],
             ["Steve", 20, "Cashier"], 
             ["Pavan", 21, "Unemployed"]]

file_path = "C:/Users/vishw/OneDrive/Desktop/Vishwas/Python/Bro Code/output.txtoutput.csv" 

try:
    with open(file_path, "w", newline="") as file:
        writer = csv.writer(file)
        for row in employees:
            writer.writerow(row)
        print(f"csv file '{file_path}' was created")

except FileExistsError:
    print("File already Exists")