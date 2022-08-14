import re
import csv

statement_data = csv.writer(open(f'data/statement_data.csv', 'w', newline='', encoding='utf8'))
statement_data.writerow(['created_at','id','lng','lat','topic','sentiment','stance','gender','temperature_avg','aggressiveness','text'])

statement_counter = 0
NUM_FILES = 16
for i in range(NUM_FILES):
    data = csv.reader(open(f'data/data_part_{i+1}_extended.csv', 'r', encoding='utf8'))
    next(data) # skip header

    for row in data:
        found_statement = False
        if re.search(r'future', row[-1]):
            # print(row[-1])
            found_statement = True
        elif re.search(r'in [\d]* years', row[-1]):
            # print(row[-1])
            found_statement = True
        elif re.search(r'[\d] years from now', row[-1]):
            # print(row[-1])
            found_statement = True
        elif re.search(r'(predicts?)|(predictions?)|(predicted)', row[-1]):
            # print(row[-1])
            found_statement = True
        elif re.search(r'will be|(is)? going to (be)?', row[-1]):
            # print(row[-1])
            found_statement = True
        elif re.search(r'(could)|(might)( not)?( be)?', row[-1]):
            # print(row[-1])
            found_statement = True
        elif re.search(r'(won\'t be)|(will not? longer (be)?)', row[-1]):
            # print(row[-1])
            found_statement = True

        if found_statement:
            statement_counter += 1
            statement_data.writerow(row)

print(statement_counter)