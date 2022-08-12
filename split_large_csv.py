'''
Script to split large data set from the paper "The climate change Twitter dataset".
As the original file contains more than 15 million entries,
it is needed to split it into smaller parts for any program to open it properly.
All part files contain the same header as the original data file.

    1. save header of data file
    2. declare file size for part files of the complete dataset
    3. iterate through dataset and save data in part files with declared size
    4. to not lose the last rows, save trailing data to another part file
'''

import csv

csv_data = csv.reader(open('data/The Climate Change Twitter Dataset.csv', 'r'))
header = next(csv_data) # skip header

MAX_FILE_SIZE = 1000000
data = []
i = 0
file_i = 1
for row in csv_data:
    data.append(row)

    i += 1
    if i % MAX_FILE_SIZE == 0:
        # write data to part file
        with open(f'data/data_part_{file_i}.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(header)
            writer.writerows(data)
        f.close()
        
        file_i += 1 # increase next file name
        data = [] # reset data list


# write trailing data to part file
with open(f'data/data_part_{file_i}.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(data)
f.close()