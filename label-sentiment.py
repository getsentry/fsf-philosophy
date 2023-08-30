#!/usr/bin/env python3
import csv
from transformers import pipeline

COMMERCIAL_TERMS = ['commerc', 'corporat', 'business', 'compan', 'money', 'saass']

guess_sentiment = pipeline(model='distilbert-base-uncased-finetuned-sst-2-english', revision='af0f99b')
fp = lambda: open('sentences.csv')
N = sum(1 for line in fp()) - 2
inp = csv.reader(fp())
headers = next(inp)

sentences = []
print(f'   0/{N}', end='')
for i, row in enumerate(inp):
    sentence = row[3]
    guess = guess_sentiment(sentence)[0]
    row[1] = guess['label'].lower()
    row[2] = guess['score']
    sentences.append(row)
    print(f'\r{i:>4}/{N} {row[0]:<9} {row[1]:>2} {str(row[2])[:3]:<5} {row[3][:48]}', end='')

print()
out = csv.writer(open('sentences.csv', 'w+'))
out.writerow(headers)
out.writerows(sentences)
