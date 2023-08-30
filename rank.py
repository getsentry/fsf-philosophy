#!/usr/bin/env python3
from collections import defaultdict

ranked = []

for line in open('html-en.txt'):
    filepath = line.strip()
    text = open(filepath, errors='ignore').read().lower()
    ncorp = 0
    for term in ('corporat', 'business', 'compan'):
        ncorp += text.count(term)
    ncomm = text.count('communit')
    nuser = text.count('user')
    n = ncorp + ncomm + nuser
    ranked.append((n, ncorp, ncomm, nuser, filepath))

for n, ncorp, ncomm, nuser, filepath in reversed(sorted(ranked)):
    print(f'{n} {ncorp} {ncomm} {nuser} {filepath}')
