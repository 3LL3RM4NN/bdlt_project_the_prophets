import csv
import pandas as pd

csv_data = csv.reader(open('data/twitter_2015-2018.csv', 'r', encoding='utf8'))
header = next(csv_data) # skip header

print(header)

data = []
i = 0
MAX_I = 20
for row in csv_data:
    # data.append(row)
    print(row)
    i += 1

    if i == MAX_I:
        break


'''
1. create dict with file number as key and tweet ids as values list (part files 3 - 14)
    save dict to json
2. for each entry in smaller tweets csv:
    find id in dict
    open corresponding file
    read corresponding line (index in values list)
    extend tweet data
3. save extended data to new csv file
'''