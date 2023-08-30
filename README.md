# Analysis of FSF Philosophy

```
wc --mirror --no-parent https://www.gnu.org/philosophy/
find www.gnu.org/philosophy -name \*.html \
  | sed -e 's/^www.gnu.org\/philosophy\///' \
  > html.txt
python3 filter-en.py > html-en.txt
ag --group communit $(cat html-en.txt) > communit.txt
ag --group compan $(cat html-en.txt) > compan.txt   
ag --group business $(cat html-en.txt) > business.txt
ag --group corporat $(cat html-en.txt) > corporat.txt
```
