'''
TODO: Script description
'''

import pandas as pd
import re


# load data to dataframe
statement_quality_data = pd.read_csv('data/random_statement_sample_manually_classified.csv', sep=',', header=0)

regex_mapping = {
    1: 'future',
    2: 'in [\d]* years',
    3: '[\d] years from now',
    4: '(predicts?)|(predictions?)|(predicted)',
    5: 'will be|(is)? going to (be)?',
    6: '(could)|(might)( not)?( be)?',
    7: '(won\'t be)|(will not? longer (be)?)'
}

regex_used = []
for row in statement_quality_data.iterrows():
        found_statement = False
        if re.search(r'future', row[-1]):
            regex_used.append(1)

        elif re.search(r'in [\d]* years', row[-1]):
            regex_used.append(2)

        elif re.search(r'[\d] years from now', row[-1]):
            regex_used.append(3)

        elif re.search(r'(predicts?)|(predictions?)|(predicted)', row[-1]):
            regex_used.append(4)

        elif re.search(r'will be|(is)? going to (be)?', row[-1]):
            regex_used.append(5)

        elif re.search(r'(could)|(might)( not)?( be)?', row[-1]):
            regex_used.append(6)

        elif re.search(r'(won\'t be)|(will not? longer (be)?)', row[-1]):
            regex_used.append(7)

assert len(regex_used) == 300

statement_quality_data['regex'] = regex_used