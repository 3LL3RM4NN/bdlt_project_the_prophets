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
