#!/usr/bin/env python3
import re
from collections import defaultdict

ranked = []

links = defaultdict(int)
pat = re.compile(r'''<a[^>]*href=["']([^"']*)["']''', re.DOTALL)

skip = '''
www.gnu.org/philosophy/essays-and-articles.html
www.gnu.org/philosophy/philosophy.html
www.gnu.org/philosophy/speeches-and-interviews.html
www.gnu.org/philosophy/third-party-ideas.html
www.gnu.org/philosophy/proprietary-surveillance.html
'''.split()

for line in open('html-en.txt'):
    filepath = line.strip()
    if filepath in skip:
        # indices and a dupe
        continue
    text = open(filepath, errors='ignore').read().lower()

    # pagerank
    for url in pat.findall(text):
        if url.startswith('/philosophy/'):
            if url.count('.') == 1:
                links[url.split('#')[0]] += 1

    # terms
    nuser = text.count('user')
    ncommunity = text.count('communit')
    ncommercial = 0
    for term in ('commerc', 'corporat', 'business', 'compan', 'money', 'saass'):
        ncommercial += text.count(term)
    n = nuser + ncommunity + ncommercial

    ranked.append([0, n, nuser, ncommunity, ncommercial, filepath])

for row in ranked:
    row[0] = links[row[5][11:]]

collated = set()
rank = lambda r, y: list(reversed(sorted(r, key=lambda x: x[y])))[:10]

for i, ranking in enumerate(('Pagerank', 'All Terms', 'User', 'Community', 'Commercial')):
    pad = ' ' * ((i * 3) + i)
    print(pad + ranking)
    print(pad + ('--v' + ('-' * (len(ranking)-3))))
    for a,b,c,d,e, filepath in rank(ranked, i):
        print(f'{a:>3} {b:>3} {c:>3} {d:>3} {e:>3} {filepath}')
        collated.add((a,b,c,d,e, filepath))
    print()

print('Collated')
print(('-v' + ('-' * (len('Collated')-2))))
for i, (a,b,c,d,e, filepath) in enumerate(reversed(sorted(collated))):
    print(f'{i+1:>2} {a:>3} {b:>3} {c:>3} {d:>3} {e:>3} {filepath}')
