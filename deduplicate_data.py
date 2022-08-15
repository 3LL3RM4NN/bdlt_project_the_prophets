'''
Script to deduplicate the data.
Since duplicates were often posted within one day,
all tweets of a single day are checked for suplicates seperately.
NOTE: This is also done due to runtime optimization.

    1. create a dictionary of the data with tweet id as key
    2. create blocks with day as key and all the ids of the day as value
    3. in each block, compare all tweets with each other and calculate similarity with bag distance
    4. keep only the originals and discard duplicate tweets
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
        

# compare texts in blocks with bag distance
THRESHOLD = 0.8

def bag_dist(val1, val2):
    # calculate the bag distance between two sets of tokens
    def bag(val:str):
        # create a mulitset used for bag distance calculation
        return Multiset(val.split(' '))

    bag_1 = bag(val1)
    bag_2 = bag(val2)

    bag_sim = 1 - (max(len(bag_1 - bag_2), len(bag_2 - bag_1)) / max(len(bag_1), len(bag_2)))

    return bag_sim

dedup_data = csv.writer(open('data/dedup_data.csv', 'w', newline='', encoding='utf8'))
dedup_data.writerow(header)
for block_key, ids in blocks.items():
    # create a helper dict for all ids contained in a block
    # set all ids to true (start with everything as original tweet, no duplicate)
    ids_in_block = {}
    for id in ids:
        ids_in_block[f'{id}'] = True

    # check every tweet for duplicates
    # if duplicate exists, set its value in helper dict to false
    # keep only the first occurence of the tweet as original
    for i, id1 in enumerate(ids):
        for id2 in ids[i:]:
            if id1 == id2:
                continue
            val1 = data_dict[id1][-1]
            val2 = data_dict[id2][-1]
            sim = bag_dist(val1, val2)

            # if two tweets are very similar, keep only the original (first occurence)
            if sim > THRESHOLD:
                ids_in_block[f'{id2}'] = False

    # keep data with True value in helper dict (originals)
    for k, v in ids_in_block.items():
        if v:
            dedup_data.writerow(data_dict[k])