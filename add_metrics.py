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

extended_header = ['tb_polarity', 'tb_subjectivity', 'hf_label', 'hf_score']
header += extended_header

classified_data = csv.writer(open('data/classified_data.csv', 'w', newline='', encoding='utf8'))
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
    score = max(scores)
    row.append(label)
    row.append(score)
    
    classified_data.writerow(row)