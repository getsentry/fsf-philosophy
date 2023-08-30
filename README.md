# Analysis of FSF Philosophy

There are 218 English-language [articles on philosophy on
gnu.org](https://www.gnu.org/philosophy/philosophy.html). A sentiment analysis
of all of the sentences from this corpus suggests that the GNU philosophy is 4x
more negative about **commerce** than about **community**. Here are the [top 30
pages on the topics of users, community, and commerce](ranked.csv):

| i | Page | Pagerank | All Terms | User | Community | Commerce |
|---:|:---|---:|---:|---:|---:|---:|
|  1 | [free-sw](https://www.gnu.org/philosophy/free-sw.html) |  56 |  48 |  25 |   4 |  19 |
|  2 | [free-software-even-more-important](https://www.gnu.org/philosophy/free-software-even-more-important.html) |  30 |  50 |  33 |   2 |  15 |
|  3 | [words-to-avoid](https://www.gnu.org/philosophy/words-to-avoid.html) |  26 | 110 |  46 |   9 |  55 |
|  4 | [open-source-misses-the-point](https://www.gnu.org/philosophy/open-source-misses-the-point.html) |  25 |  51 |  33 |   8 |  10 |
|  5 | [who-does-that-server-really-serve](https://www.gnu.org/philosophy/who-does-that-server-really-serve.html) |  20 | 115 |  30 |   2 |  83 |
|  6 | [categories](https://www.gnu.org/philosophy/categories.html) |  18 |  34 |  11 |   1 |  22 |
|  7 | [not-ipr](https://www.gnu.org/philosophy/not-ipr.html) |  14 |   5 |   2 |   0 |   3 |
|  8 | [why-call-it-the-swindle](https://www.gnu.org/philosophy/why-call-it-the-swindle.html) |  13 |  13 |   9 |   0 |   4 |
|  9 | [javascript-trap](https://www.gnu.org/philosophy/javascript-trap.html) |   9 |  21 |  18 |   2 |   1 |
| 10 | [surveillance-vs-democracy](https://www.gnu.org/philosophy/surveillance-vs-democracy.html) |   8 |  51 |  21 |   0 |  30 |
| 11 | [copyright-and-globalization](https://www.gnu.org/philosophy/copyright-and-globalization.html) |   3 |  90 |   9 |   2 |  79 |
| 12 | [copyright-versus-community](https://www.gnu.org/philosophy/copyright-versus-community.html) |   3 |  84 |  22 |  23 |  39 |
| 13 | [rms-nyu-2001-transcript](https://www.gnu.org/philosophy/rms-nyu-2001-transcript.html) |   2 | 187 |  45 |  42 | 100 |
| 14 | [copyright-versus-community-2000](https://www.gnu.org/philosophy/copyright-versus-community-2000.html) |   2 |  65 |   5 |  15 |  45 |
| 15 | [pragmatic](https://www.gnu.org/philosophy/pragmatic.html) |   2 |  21 |   5 |  12 |   4 |
| 16 | [proprietary-surveillance](https://www.gnu.org/philosophy/proprietary/proprietary-surveillance.html) |   1 | 363 | 274 |   0 |  89 |
| 17 | [stallman-mec-india](https://www.gnu.org/philosophy/stallman-mec-india.html) |   1 | 123 |  21 |  15 |  87 |
| 18 | [free-digital-society](https://www.gnu.org/philosophy/free-digital-society.html) |   1 | 113 |  40 |   1 |  72 |
| 19 | [google-engineering-talk](https://www.gnu.org/philosophy/google-engineering-talk.html) |   1 | 108 |  62 |  11 |  35 |
| 20 | [malware-microsoft](https://www.gnu.org/philosophy/proprietary/malware-microsoft.html) |   1 |  99 |  85 |   0 |  14 |
| 21 | [nit-india](https://www.gnu.org/philosophy/nit-india.html) |   1 |  95 |  43 |   7 |  45 |
| 22 | [danger-of-software-patents](https://www.gnu.org/philosophy/danger-of-software-patents.html) |   1 |  94 |  13 |   2 |  79 |
| 23 | [malware-apple](https://www.gnu.org/philosophy/proprietary/malware-apple.html) |   1 |  89 |  76 |   0 |  13 |
| 24 | [ough-interview](https://www.gnu.org/philosophy/ough-interview.html) |   1 |  87 |  29 |  16 |  42 |
| 25 | [rms-hack](https://www.gnu.org/philosophy/rms-hack.html) |   1 |  72 |   2 |  32 |  38 |
| 26 | [moglen-harvard-speech-2004](https://www.gnu.org/philosophy/moglen-harvard-speech-2004.html) |   1 |  54 |   6 |   2 |  46 |
| 27 | [rms-interview-edinburgh](https://www.gnu.org/philosophy/rms-interview-edinburgh.html) |   1 |  46 |  16 |  10 |  20 |
| 28 | [android-and-users-freedom](https://www.gnu.org/philosophy/android-and-users-freedom.html) |   1 |  44 |  43 |   0 |   1 |
| 29 | [digital-inclusion-in-freedom](https://www.gnu.org/philosophy/digital-inclusion-in-freedom.html) |   0 |  69 |  42 |   1 |  26 |
| 30 | [free-software-for-freedom](https://www.gnu.org/philosophy/free-software-for-freedom.html) |   0 |  54 |  17 |  12 |  25 |


## How to Run

Depends on wget (thank you GNU! :) and Python 3.

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

./report.py
```

```
Dropped 231 sentences out of 2129 for low confidence, 1898 remaining.

           neg /  pos
commerce  1288 /  284 = 5
community  180 /  146 = 1
                     /= 4

The GNU philosophy is 4x more negative about commerce than about community.
```
