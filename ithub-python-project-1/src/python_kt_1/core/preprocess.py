import pathlib
from string import punctuation, whitespace
import ru_core_news_lg
from nltk.stem.porter import *
from .tokenize import tokenize_text

extended_punctuation = punctuation + '«»—-…'

def _load_stopwords() -> set:
    path_to_file = pathlib.Path() / 'src' / 'python_kt_1' / 'core' / "stopwords.txt"
    f = open(path_to_file, encoding='utf-8')
    stopwords = f.read().splitlines()
    f.close()
    return set(stopwords)

def filter_stopwords(words: list[str]) -> list[str]:
    stopwords_lower = _load_stopwords()
    stopwords_title = set([stopword.title() for stopword in stopwords_lower])
    return [word for word in words if word and word not in stopwords_lower | stopwords_title]

def clean_words(words: list[str]) -> list[str]:
    return [word.strip(punctuation + whitespace + extended_punctuation) for word in words]

def lemmatization(words: list[str]) -> list[str]:
    nlp = ru_core_news_lg.load()
    doc = nlp(' '.join(words))
    return [l.lemma_ for l in doc]

def stamming(words: list[str]) -> list[str]:
    stemmer = PorterStemmer()
    return [stemmer.stem(l) for l in words]