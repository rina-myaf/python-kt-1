from ..core.preprocess import filter_stopwords, clean_words, lemmatization, stamming
from typing import Literal
from ..core.tokenize import tokenize_text

def _count_words(words: list[str]) -> dict [str, int]:
    counter = {}
    for word in words:
        if word not in counter:
            counter[word] = 1
        else:
            counter[word] += 1
            
    return counter

def sort_by_count(item: tuple[str, int]) -> int:
    return -item[1]

def top_words(
    text:str,
    normalize_mode: Literal["stemming", "lemmatization"] = "lemmatization",
    pos: list[str] = ["__all__"]):
    
    
    initial_words = tokenize_text(text)["words"]
    words_after_clean = clean_words(initial_words)
    words_after_filter = filter_stopwords(words_after_clean)
    if normalize_mode == 'lemmatization':
        normalize_words = lemmatization(words_after_filter)
    else: normalize_words = stamming(words_after_filter)

    clean_normalize_words = clean_words(normalize_words)    
    sorted_words_counter = sorted(_count_words(clean_normalize_words).items(), key=sort_by_count)
    
    print(sorted_words_counter)
    return sorted_words_counter

    """Подсчет топ-N-важных слов.

    Получает текст, разбивает на слова, убирает пунктуацию и пробельные символы,
    фильтрует стоп-слова, нормализует (стемминг/лемматизация),
    подсчитывает и возвращает список картежей для топ-N-важных слов.
    """
