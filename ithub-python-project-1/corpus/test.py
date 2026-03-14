import re
import pathlib
import typing

from ..src.python_kt_1.core.types import SearchResult

def re_search(pattern: str, file_path: pathlib.Path, is_regex: bool = True
) -> typing.Iterable[SearchResult]:
    text = file_path.read_text(encoding="utf-8")
    match = re.find(pattern, text)
    print(match)

    re_search(text, 'corpus/1.txt' 'corpus/3.txt', True)
    