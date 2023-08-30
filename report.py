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
ntotal = 0

for bucket, sentiment, score, sentence in inp:
    assert sentiment in ('positive', 'negative'), sentiment
    ntotal += 1
    if float(score) < 0.9:
        ndropped += 1
        continue
    buckets[bucket][sentiment] += 1

print(f'Dropped {ndropped} sentences out of {ntotal} for low confidence, {ntotal - ndropped} remaining.')
print()

print(f'{"":<9} {"neg":>4} / {"pos":>4}')
for bucket in ('commerce', 'community'):
    vals = buckets[bucket]
    neg = vals['negative']
    pos = vals['positive']
    ratio = buckets[bucket]['ratio'] = neg / pos
    print(f'{bucket:<9} {neg:>4} / {pos:>4} = {round(ratio)}')

community = buckets['community']['ratio']
commerce = buckets['commerce']['ratio']
pref = commerce / community
print(f'                     /= {round(pref)}')
print()

print(f"The GNU philosophy is {round(pref)}x more negative about commerce than about community.")
