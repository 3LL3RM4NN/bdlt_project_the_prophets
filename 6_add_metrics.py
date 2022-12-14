'''
Script to add classification metrics to the data.
Classification with TextBlob (polarity and subjectivity).
Classification with the latest Twitter Roberta Model available at HuggingFace (label and highest score).

    1. load model for classification
    2. prepare new file for extended data
    3. sentiment score tweet text with TextBlob and append metrics to data
    4. score tweets text with Twitter Roberta Model and append metrics to data
'''

import csv
from textblob import TextBlob
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from scipy.special import softmax
import numpy

MODEL = "cardiffnlp/twitter-roberta-base-sentiment-latest"
LABELS = ['negative', 'neutral', 'positive']

tokenizer = AutoTokenizer.from_pretrained(MODEL)
model = AutoModelForSequenceClassification.from_pretrained(MODEL)

deduped_data = csv.reader(open('data/dedup_data.csv', 'r', encoding='utf8'))
header = next(deduped_data) # skip header

extended_header = ['tb_polarity', 'tb_subjectivity', 'hf_label', 'hf_score_neg', 'hf_score_neutral', 'hf_score_pos']
header += extended_header

classified_data = csv.writer(open('data/classified_data_1.csv', 'w', newline='', encoding='utf8'))
classified_data.writerow(header)

for row in deduped_data:
    text = row[-1]

    blob = TextBlob(text)
    row.append(blob.sentiment.polarity)
    row.append(blob.sentiment.subjectivity)

    encoded_input = tokenizer(text, return_tensors='pt')
    output = model(**encoded_input)
    scores = output[0][0].detach().tolist()
    scores = softmax(scores)

    label = LABELS[numpy.argmax(scores)]
    score_neg = scores[0]
    score_neutral = scores[1]
    score_pos = scores[2]
    row.append(label)
    row.append(score_neg)
    row.append(score_neutral)
    row.append(score_pos)
    
    classified_data.writerow(row)