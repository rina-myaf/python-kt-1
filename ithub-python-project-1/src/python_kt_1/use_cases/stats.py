import re
from string import punctuation
import json
import pathlib

import ru_core_news_lg

from ..core.types import TextStats, SymbolStats, TokensStats, PosStats


def stats(text: str, pos: bool = False) -> TextStats:
    from ..cli.renderer import display_stats
    """Функция для подсчета статистик.

    Args:
        text: текст для расчета статистик
        pos: опция, добавляет аналитику по частям речи

    Returns:
        Статистика, сгруппированная по токенам, символам и,
        опционально, морфологическим характеристикам

        Например, для строки `\tПроверка!\nНовая строка` это
        будет:
        {
            "tokens": {
                "paragraphs": 2,
                "sentences": 2,
                "words": 3,
            },
            "symbols": {
                "alphas": {
                    "quantity": 19,
                    "percent": 82.61
                },
                "digits": {
                    "quantity": 0,
                    "percent": 0.00
                },
                "spaces": {
                    "quantity": 3,
                    "percent": 13.04
                },
                "punctuation": {
                    "quantity": 1,
                    "percent": 4.35
                }
            }
        }

    """

    return {display_stats(text)}


def _get_symbols_stats(text: str) -> SymbolStats:
    """Посимвольная статистика (количество и процент)."""

    count_alphas = 0
    count_digits = 0
    count_spaces = len(re.findall(r'\s', text)) 
    count_punctuation = 0
    extended_punctuation = punctuation + '«»—'
    for symbol in text:
        if symbol.isalpha():
            count_alphas += 1
        if symbol.isdigit():
            count_digits += 1
        if symbol in extended_punctuation:
            count_punctuation += 1
        
    return {
        "alphas": {"quantity": count_alphas, "percent": round(count_alphas / len(text), 2)},
        "digits": {"quantity": count_digits, "percent": round(count_digits / len(text), 2)},
        "spaces": {"quantity": count_spaces, "percent": round(count_spaces / len(text), 2)},
        "punctuation": {"quantity": count_punctuation, "percent": round(count_punctuation / len(text), 2)},
    }


def _get_tokens_stats(text: str) -> TokensStats:
    """Подсчет количества токенов."""
    text = text.strip()

    return {
        "paragraphs": len(text.splitlines()),
        "sentences": len(re.split(r'[.?!]'+ r'\s+', text)),
        "words": len(re.split(r'\s+' or [punctuation + '«»—'], text))
    }

def _get_pos_stats(text: str) -> PosStats:
    """Подсчет pos-аналитики"""
    nlp = ru_core_news_lg.load()
    doc = nlp(text)
    adj = 0
    cconj = 0
    adv = 0
    adp = 0
    noun = 0
    verb = 0
    det = 0
    part = 0
    for token in doc:
        if token.pos_ != 'PUNCT' and token.pos_ != 'NUM':
            if token.pos_ == 'ADJ':
                adj += 1
            elif token.pos_ == 'VERB':
                verb += 1
            elif token.pos_ == 'NOUN' or token.pos_ == 'PROPN':
                noun += 1
            elif token.pos_ == 'ADV':
                adv += 1
            elif token.pos_ == 'CCONJ':
                cconj += 1
            elif token.pos_ == 'ADP':
                adp += 1
            elif token.pos_ == 'DET' or token.pos_ == 'PRON':
                det += 1
            elif token.pos_ == 'PART' or token.pos_ == 'SCONJ':
                part += 1
    return {
        "nouns": noun,
        "adjectives": adj,
        "verbs": verb,
        "adverbs": adv,
        'conjunction': cconj,
        'preposition': adp,
        'pronoun': det,
        'particles': part   
    }