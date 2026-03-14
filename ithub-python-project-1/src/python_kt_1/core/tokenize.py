import re
from .types import Tokens

def _get_words(text: str) -> list[str]:
    return re.split(r'\s+', text)

def _get_paragraphs(text: str) -> list[str]:
    return re.split(r'\n', text)

def _get_sentences(text: str) -> list[str]:
    return re.split(r'[.?!]'+ r'\s+', text)

def tokenize_text(text: str) -> Tokens:
    
    """Разбиение текста на токены.

    Разбиение текста на токены:
    - параграфы (абзацы),
    - предложения,
    - слова
    """

    return {
        "paragraphs": _get_paragraphs(text),
        "sentences": _get_sentences(text),
        "words": _get_words(text),
    }
