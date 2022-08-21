'''
Script to select random rows from deduped data for manual classification (is a statement for future?).

    1. generate random entrie nums to select
    2. load deduped data
    3. select the randomly chosen rows
    4. write rows to new file
'''

import csv
import numpy as np

DATA_ENTRIES = 68283
DATA_FILE = 'data/dedup_data.csv'

# generate random entries to keep for manual classification
np.random.seed(334) # make it reproducable
random_entries = np.sort(np.random.choice(DATA_ENTRIES, 300))

# load deduped data
deduped_data = csv.reader(open(DATA_FILE, 'r', encoding='utf8'))
header = next(deduped_data) # skip header

# take the rows previously generated
random_rows = []
row_count = 0
random_entry_count = 0
for row in deduped_data:
    if random_entries[random_entry_count] == row_count:
        random_rows.append(row)
        random_entry_count += 1
        if random_entry_count >= len(random_entries):
            break
    
    row_count += 1

# write rows to csv
random_statement_sample = csv.writer(open(f'data/random_statement_sample.csv', 'w', newline='', encoding='utf8'))
random_statement_sample.writerow(header)
random_statement_sample.writerows(random_rows)
