from wordcloud import WordCloud
from ..core.preprocess import filter_stopwords
from typing import Literal

def word_cloud(
    text:str,
    preprocess_mode: Literal["basic", "stemming", "lemmatization"] = "stemming"):
    if preprocess_mode == 'basic':
        cloud = WordCloud().generate(text).to_file()
    return