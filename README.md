# Analysis of FSF Philosophy



## How to Run

Depends on wget and Python 3.

```
python3 -m venv .env --prompt='fsf'
source .env/bin/activate
pip install --upgrade --requirement requirements.txt

wget --mirror --no-parent https://www.gnu.org/philosophy/
find www.gnu.org/philosophy -name \*.html \
  | sed -e 's/^www.gnu.org\/philosophy\///' \
  > html.txt
./filter-en.py > html-en.txt
./rank.py > ranked.txt
./find-sentences.py > sentences.txt
./prep-csv.py > sentences.csv

# https://huggingface.co/blog/sentiment-analysis-python
time ./label-sentiment.py # modifies sentences.csv
```
