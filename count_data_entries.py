'''
Script to count the entries in the different stages of the data.
The original data is from the paper "The climate change Twitter dataset"

    1. count entries in the original data
    2. count entries in extended date
'''

import csv

# --- original data ---------------------------------------------------------------------------------------
# open original data file
original_data = csv.reader(open('data/The Climate Change Twitter Dataset.csv', 'r'))
next(original_data) # skip header

# count the entries of the original data
original_entries_count = sum(1 for _ in original_data)
print(f'Data count original data: {original_entries_count}') # 15.789.411


# --- extended data ---------------------------------------------------------------------------------------
extended_data_count = []
NUM_FILES = 16
for i in range(NUM_FILES):
    # open extended data file
    extended_data = csv.reader(open(f'data/data_part_{i+1}_extended.csv', 'r', encoding='utf8'))
    next(extended_data) # skip header

    # append data count of each file
    extended_data_count.append(sum(1 for _ in extended_data))

extended_data_count = sum(extended_data_count)
print(f'Data count extended data: {extended_data_count}') # 1.942.438


# --- filtered data ---------------------------------------------------------------------------------------
# open filtered data file
filtered_data = csv.reader(open('data/clean_statement_data.csv', 'r', encoding='utf8'))
next(filtered_data) # skip header

# count the entries of the filtered data
filtered_entries_count = sum(1 for _ in filtered_data)
print(f'Data count original data: {filtered_entries_count}') # 109.247


# --- deduped data ----------------------------------------------------------------------------------------
# open deduped data file
deduped_data = csv.reader(open('data/dedup_data.csv', 'r', encoding='utf8'))
next(deduped_data) # skip header

# count the entries of the deduped data
deduped_entries_count = sum(1 for _ in deduped_data)
print(f'Data count original data: {deduped_entries_count}') # 68.283