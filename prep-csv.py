#!/usr/bin/env python3
import csv, sys

COMMUNITY_TERMS = ['communit', 'collective']
COMMERCIAL_TERMS = ['commerc', 'corporat', 'business', 'compan', 'money', 'saass']
out = csv.writer(sys.stdout)
out.writerow(('bucket', 'sentiment', 'score', 'sentence'))

ncommunity = ncommerce = 0

for line in open('sentences.txt'):
    sentence = line.strip()
    any_community = any([term in sentence for term in COMMUNITY_TERMS])
    any_commerce = any([term in sentence for term in COMMERCIAL_TERMS])
    if any_community and not any_commerce:
        bucket = 'community'
        ncommunity += 1
    elif not any_community and any_commerce:
        bucket = 'commerce'
        ncommerce += 1
    else:
        continue
    out.writerow([bucket, '', '', sentence])

print(ncommunity, ncommerce, file=sys.stderr)
