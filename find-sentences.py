#!/usr/bin/env python3
import re

pat_comment = re.compile('<!--.*?-->', re.DOTALL)
pat_heading = re.compile('</h\d>')
pat_tag = re.compile('<.*?>', re.DOTALL)
pat_spaces = re.compile(' +')
pat_sentence = re.compile(r'''(\S\S[.?!]["' ])''')

for line in open('html-en.txt'):
    filepath = line.strip()
    if filepath == 'www.gnu.org/philosophy/amazonpatent.html':
        continue # skip patent filing

    text = open(filepath, errors='ignore')
    content = []

    in_head = True
    for line in text:
        line = line.strip()
        if not line:
            continue
        elif line.startswith('</div><!-- for id="content"'):
            break
        elif in_head:
            if line.startswith('<div class="article'):
                in_head = False
            continue
        elif line.startswith('<address class="byline">'):
            continue
        content.append(line)
    if not content:
        print(filepath)
        continue

    text = ' '.join(content).lower()
    text = pat_comment.sub(' ', text)
    text = pat_heading.sub('.', text)
    text = pat_tag.sub('', text)
    text = pat_spaces.sub(' ', text)
    text = text.replace('&hellip;', '…')
    text = text.replace('&mdash;', '—')
    text = text.replace('&amp;', '&')
    text = text.replace('&nbsp;', ' ')
    text = text.replace('&lsquo;', '"')
    text = text.replace('&rsquo;', '"')
    text = text.replace('&ldquo;', '"')
    text = text.replace('&rdquo;', '"')
    text = text.replace('&lt;', '<')
    text = text.replace('&gt;', '>')
    text = pat_sentence.sub('\\1\n', text)
    text = '\n'.join([x for x in text.splitlines() if x.strip()])
    print(text)
