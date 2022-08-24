'''
Script to extract statistics about the different datasets in order to compare them

Statistics include value counts for
    - aggressiveness
    - stance
    - gender
    - topic 

for each of the following dataset variants
    - sampled original data
    - statement data
    - deduplicated (and classified) statements

Results are printed to stdout
'''

import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

NUM_FILES = 16

data = pd.read_csv(f'data/data_part_{1}.csv', sep=',', header=0)
data['created_at'] = pd.to_datetime(data['created_at'])

aggressiveness_counts =  data['aggressiveness'].value_counts()
stance_counts =  data['stance'].value_counts()
topic_counts =  data['topic'].value_counts()
gender_counts =  data['gender'].value_counts()

for i in range(1,NUM_FILES):

    data = pd.read_csv(f'data/data_part_{i+1}.csv', sep=',', header=0)
    data['created_at'] = pd.to_datetime(data['created_at'])

    aggressiveness_counts +=  data['aggressiveness'].value_counts()
    stance_counts +=  data['stance'].value_counts()
    topic_counts +=  data['topic'].value_counts()
    gender_counts +=  data['gender'].value_counts()

print("####### Sampled Data ###########")
print(aggressiveness_counts)
print(stance_counts)
print(topic_counts)
print(gender_counts)


# --------------------------------------------------------------------------------------------------
data = pd.read_csv(f'data/data_part_{1}_extended.csv', sep=',', header=0)
data['created_at'] = pd.to_datetime(data['created_at'])

aggressiveness_counts =  data['aggressiveness'].value_counts()
stance_counts =  data['stance'].value_counts()
topic_counts =  data['topic'].value_counts()
gender_counts =  data['gender'].value_counts()

for i in range(1,NUM_FILES):

    data = pd.read_csv(f'data/data_part_{i+1}_extended.csv', sep=',', header=0)
    data['created_at'] = pd.to_datetime(data['created_at'])

    aggressiveness_counts +=  data['aggressiveness'].value_counts()
    stance_counts +=  data['stance'].value_counts()
    topic_counts +=  data['topic'].value_counts()
    gender_counts +=  data['gender'].value_counts()

print("####### Sampled Data ###########")
print(aggressiveness_counts)
print(stance_counts)
print(topic_counts)
print(gender_counts)


# --------------------------------------------------------------------------------------------------
data = pd.read_csv(f'data/statement_data.csv', sep=',', header=0)
data['created_at'] = pd.to_datetime(data['created_at'])

aggressiveness_counts =  data['aggressiveness'].value_counts()
stance_counts =  data['stance'].value_counts()
topic_counts =  data['topic'].value_counts()
gender_counts =  data['gender'].value_counts()

print("###### Statement data ##############")
print(aggressiveness_counts)
print(stance_counts)
print(topic_counts)
print(gender_counts)

aggressiveness_counts =  data['aggressiveness'].value_counts(normalize=True)
stance_counts =  data['stance'].value_counts(normalize=True)
topic_counts =  data['topic'].value_counts(normalize=True)
gender_counts =  data['gender'].value_counts(normalize=True)

print("###### Statement data percentages ##############")
print(aggressiveness_counts)
print(stance_counts)
print(topic_counts)
print(gender_counts)


# --------------------------------------------------------------------------------------------------
data = pd.read_csv(f'data/classified_data.csv', sep=',', header=0)
data['created_at'] = pd.to_datetime(data['created_at'])

aggressiveness_counts =  data['aggressiveness'].value_counts()
stance_counts =  data['stance'].value_counts()
topic_counts =  data['topic'].value_counts()
gender_counts =  data['gender'].value_counts()

print("###### Classified data ##############")
print(aggressiveness_counts)
print(stance_counts)
print(topic_counts)
print(gender_counts)

aggressiveness_counts =  data['aggressiveness'].value_counts(normalize=True)
stance_counts =  data['stance'].value_counts(normalize=True)
topic_counts =  data['topic'].value_counts(normalize=True)
gender_counts =  data['gender'].value_counts(normalize=True)

print("###### Classified data percentages ##############")
print(aggressiveness_counts)
print(stance_counts)
print(topic_counts)
print(gender_counts)