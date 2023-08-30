# Analysis of FSF Philosophy

```
wc --mirror --no-parent https://www.gnu.org/philosophy/
find www.gnu.org/philosophy -name \*.html \
  | sed -e 's/^www.gnu.org\/philosophy\///' \
  > html.txt
python3 filter-en.py > html-en.txt
python3 rank.py > ranked.txt
```
