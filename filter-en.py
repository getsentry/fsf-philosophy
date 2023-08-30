#!/usr/bin/env python3
import difflib

fp = open('html.txt')
has = set()
hasnt = set()
weird = set()

for line in fp:
    line = line.strip()
    slug, rest = line.split('.', 1)
    if '.' in rest:
        one, two = rest.split('.')
        if one == 'html':
            bucket = weird
            lang = two
        else:
            bucket = has
            lang = one
        if lang != 'en':
            continue
    else:
        bucket = hasnt
    bucket.add(slug)

base = 'www.gnu.org/philosophy/'
prefix = '   <a href="/server/select-language.html?callback=/philosophy/'

for slug in sorted(hasnt):
    filepath = base + f'{slug}.html'
    for bucket, alt in ((has, f'{slug}.en.html'), (weird, f'{slug}.html.en')):
        if slug in bucket:
            bucket.remove(slug)
            a = open(filepath).readlines()
            b = open(base + alt).readlines()
            diff = list(difflib.unified_diff(a, b))
            derp = False
            for line in diff[3:]:
                if line.startswith(' '):
                    continue
                elif line[0] in '-+' and line[1:].startswith(prefix):
                    # Ensure we only differ in the select-language link href.
                    continue
                else:
                    derp = True
            if derp:
                print(''.join(diff))
                raise heck

    print(f'{slug}.html')

# Everything in these should have also been in hasnt.
assert not has, has
assert not weird, weird
