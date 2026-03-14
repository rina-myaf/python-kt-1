from rich.console import Console
from rich.table import Table
from ..use_cases.stats import _get_symbols_stats, _get_tokens_stats, _get_pos_stats

console = Console()

def display_stats(text: str, title: str = "Статистикa"):
    
    symbol_stats = _get_symbols_stats(text)
    token_stats = _get_tokens_stats(text)
    pos_stats = _get_pos_stats(text)
    
    console.print(f"\n[bold cyan]{title}[/bold cyan]")
    console.print(f"Длина текста: {len(text)} символов\n")
    
    table = Table(show_header=True, header_style="bold")
    table.add_column("Показатель")
    table.add_column("Значение", justify="right")
    
    for key, name in [("alphas", "Буквы"), ("digits", "Цифры"), 
                      ("spaces", "Пробелы"), ("punctuation", "Пунктуация")]:
        table.add_row(name, str(symbol_stats[key]["quantity"]))
    
    for key, name in [('paragraphs', 'Параграфы'),
                      ('sentences', 'Предложения'),
                      ('words', 'Слова')]:
        table.add_row(name, str(token_stats[key]))
    for key, name in [('nouns', 'Существительные'), ('adjectives', 'Прилагательные'),
                      ('verbs', 'Глаголы'), ('adverbs', 'Наречия'), ('conjunction', "Союзы"),
                      ('preposition', "Предлоги"), ('pronoun', 'Местоимения'), ('particles', "Частицы")]:
        table.add_row(name, str(pos_stats[key]))
    
    console.print(table)