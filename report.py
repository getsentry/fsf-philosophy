#!/usr/bin/env python3
import csv

NEGATIVE, NEUTRAL, POSITIVE = (-1, 0, 1)
inp = csv.reader(open('sentences.csv'))
headers = next(inp)

buckets = {
    'community': {
        'positive': 0,
        'negative': 0,
    },
    'commerce': {
        'positive': 0,
        'negative': 0,
    },
}

ndropped = 0

for bucket, sentiment, score, sentence in inp:
    assert sentiment in ('positive', 'negative'), sentiment
    if float(score) < 0.9:
        ndropped += 1
        continue
    buckets[bucket][sentiment] += 1

print(f'dropped {ndropped} for low confidence')
for bucket, vals in buckets.items():
    neg = buckets[bucket]['negative']
    pos = buckets[bucket]['positive']
    ratio = buckets[bucket]['ratio'] = neg / pos
    print(f'{bucket:<9} {neg:>4} / {pos:>4} = {ratio:>3.1f}')

community = buckets['community']['ratio']
commerce = buckets['commerce']['ratio']
pref = commerce / community
print(f'{community:>3.1f} / {commerce:>3.1f} = {pref:>3.1f}x more likely to speak negatively about commerce than about community')
