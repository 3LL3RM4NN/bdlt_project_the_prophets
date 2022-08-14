'''
TODO: script description
'''

'''
plan:
    1. dict key = tweet_id, value = complete csv row (list)
    2. blocking with date (block every day)
    3. if duplicate: keep only tweet with smaller id
    4. assemble reduced dataset
'''

import csv
from collections import defaultdict
from multiset import Multiset

cleaned_data = csv.reader(open('data/clean_statement_data.csv', 'r', encoding='utf8'))
header = next(cleaned_data) # skip header

# build dict
data_dict = {}
for row in cleaned_data:
    data_dict[f'{row[1]}'] = row


# create blocks
blocks = defaultdict(list)
for k, v in data_dict.items():
    blocks[f'{v[0].split()[0]}'].append(k)
        
#print(blocks['2018-10-01'])

# compare texts in blocks with bag distance
THRESHOLD = 0.8

def bag_dist(val1, val2):
    def bag(val:str):
        return Multiset(val.split(' '))

    bag_1 = bag(val1)
    bag_2 = bag(val2)

    bag_sim = 1 - (max(len(bag_1 - bag_2), len(bag_2 - bag_1)) / max(len(bag_1), len(bag_2)))

    return bag_sim

dedup_data = csv.writer(open('data/dedup_data.csv', 'w', newline='', encoding='utf8'))
dedup_data.writerow(header)
for block_key, ids in blocks.items():
    ids_in_block = {}
    for id in ids:
        ids_in_block[f'{id}'] = True

    for i, id1 in enumerate(ids):
        for id2 in ids[i:]:
            if id1 == id2:
                continue
            val1 = data_dict[id1][-1]
            val2 = data_dict[id2][-1]
            sim = bag_dist(val1, val2)

            if sim > THRESHOLD:
                ids_in_block[f'{id2}'] = False

    for k, v in ids_in_block.items():
        if v:
            dedup_data.writerow(data_dict[k])