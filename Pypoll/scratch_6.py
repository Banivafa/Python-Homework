
import os


import csv
print(os.getcwd())
csvpath: str = 'C:/Users/anous/Downloads/Pypoll.csv'
csv_str = os.path.join('C:', 'Users', 'anous' , 'Downloads', 'Pypoll.csv' )

with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)


    csv_header = next (csvreader)
    print(f"CSV Header: {csvheader}")
    for row in csvreader:
        print(row)