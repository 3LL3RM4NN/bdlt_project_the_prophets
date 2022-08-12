'''
Script to gather the tweets text of the dataset from the paper "The climate change Twitter dataset".
Because of the limitations of the Twitter API, not every tweet of the original dataset is scraped.
The Twitter accounts used for scraping are remainders of the Bachelors Thesis of Julius Ellermann.
Script is called via commandline where the Twitter Account and the file to work through are declared.

    1. get arguments from commandline call (Twitter account and file number)
    2. read Twitter credentials from corrsponding file
    3. save credentials and create Twitter API
    4. open file to scrape tweets for
    5. scrape every 8th tweet (API Limits) and save extended data to new file
'''

import argparse
import csv
import tweepy

# example call
# python .\get_tweets_for_ids.py -t twitter_cred/Baymax.csv -f 1
# python .\get_tweets_for_ids.py -t twitter_cred/BB8.csv -f 2
# python .\get_tweets_for_ids.py -t twitter_cred/Bumblebee.csv -f 3
# python .\get_tweets_for_ids.py -t twitter_cred/C3PO.csv -f 4
# python .\get_tweets_for_ids.py -t twitter_cred/R2D2.csv -f 5
# python .\get_tweets_for_ids.py -t twitter_cred/WallE.csv -f 6

parser = argparse.ArgumentParser()
parser.add_argument('-t', '--twitter', help='path to twitter api credentials .json', type=str)
parser.add_argument('-f', '--file', help='data file to extend with tweet texts', type=int)
args = parser.parse_args()

# get twitter api credentials from csv
with open(args.twitter, newline='') as cred_csv_file:
    api_access = csv.reader(cred_csv_file, delimiter=',')
    # skip first row
    next(api_access)
    cred = next(api_access)
    cred_csv_file.close()

API_KEY = cred[0]
API_SECRET = cred[1]
ACCESS_TOKEN = cred[2]
ACCESS_TOKEN_SECRET = cred[3]

# sign into twitter api
auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth, wait_on_rate_limit=True)

# read large csv file to extend with tweet texts
csv_data = csv.reader(open(f'data/data_part_{str(args.file)}.csv', 'r', newline=''))
header = next(csv_data)
header.append('text')

# create file with extended data
extended_data_writer = csv.writer(open(f'data/data_part_{args.file}_extended.csv', 'w', newline='', encoding='utf8'))
extended_data_writer.writerow(header)

# scrape text of every 8th tweet
SKIP_TWEETS = 8 - 1 
for row in csv_data:
    tweet_id = row[1]
    try:
        tweet_text = api.get_status(tweet_id).text
    except:
        continue
    
    # extend data with tweet text
    extended_row = row
    extended_row.append(tweet_text)

    # immedeately write row
    extended_data_writer.writerow(extended_row)

    # skip a few rows
    for _ in range(SKIP_TWEETS):
        next(csv_data)

