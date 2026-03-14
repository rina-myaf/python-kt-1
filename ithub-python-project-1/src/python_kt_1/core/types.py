from typing import TypedDict, Iterable


class QuantityPercent(TypedDict):
    quantity: int
    percent: float


class SymbolStats(TypedDict):
    alphas: QuantityPercent
    digits: QuantityPercent
    spaces: QuantityPercent
    punctuation: QuantityPercent


class TokensStats(TypedDict):
    paragraphs: int
    sentences: int
    words: int
    
class PosStats(TypedDict):
    nouns: int
    adjectives: int
    verbs: int
    adverbs: int
    conjunction: int
    preposition: int
    pronoun: int
    particles: int

class TextStats(TypedDict):
    tokens: TokensStats
    symbols: SymbolStats


class SearchResult(TypedDict):
    result: str
    start: int
    end: int


class Tokens(TypedDict):
    paragraphs: Iterable[str]
    sentences: Iterable[str]
    words: Iterable[str]

