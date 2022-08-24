'''
Script to clean (possible) statements about the future.

    1. make all text lowercase
    2. remove emojis
    3. remove newlines and tabs
    4. replace links with "LINK" keyword
    5. replace user @mention with "USER_REF" keyword
    6. remove structures in form of &amp;
    7. remove all kind of trailing ticks and special forms of them
    8. replace multiple spaces with a single one
'''

import csv
import re

def de_emojify(text):
    # function to remove (hopefully) any emoji
    emoj = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
        u"\U00002500-\U00002BEF"  # chinese char
        u"\U00002702-\U000027B0"
        u"\U00002702-\U000027B0"
        u"\U000024C2-\U0001F251"
        u"\U0001f926-\U0001f937"
        u"\U00010000-\U0010ffff"
        u"\u2640-\u2642" 
        u"\u2600-\u2B55"
        u"\u200d"
        u"\u23cf"
        u"\u23e9"
        u"\u231a"
        u"\ufe0f"  # dingbats
        u"\u3030"
                      "]+", re.UNICODE)
    return re.sub(emoj, '', text)


future_data = csv.reader(open(f'data/statement_data.csv', 'r', encoding='utf8'))
header = next(future_data) # skip header

clean_future_data = csv.writer(open(f'data/clean_statement_data.csv', 'w', newline='', encoding='utf8'))
clean_future_data.writerow(header)

for row in future_data:
    text = row[-1]

    text = text.lower()
    text = de_emojify(text)
    text = re.sub("\n|\r", "", text)
    text = re.sub(r"http\S+", "LINK", text, flags=re.MULTILINE)
    text = re.sub(r"www.\S+", "LINK", text, flags=re.MULTILINE)
    text = re.sub(r"@[A-Za-z0-9_]+", "USER_REF", text)
    text = re.sub(r'&\S+;', '', text)
    text = re.sub(r'^"|“', '', text)
    text = re.sub(r'"|“$', '', text)
    text = re.sub(r'‘|’', '\'', text)
    text = re.sub(r' ', '', text)
    text = re.sub(r'^"', '', text)
    text = re.sub(r'"$', '', text)
    text = re.sub(r'^\"', '', text)
    text = re.sub(r'\"$', '', text)
    text = text.strip()
    text = text.strip('"“”')
    text = re.sub(r'/\s{2,}/g', ' ', text)

    row[-1] = text
    clean_future_data.writerow(row)
