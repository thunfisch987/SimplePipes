"""Module enabling a sh like infix syntax (using pipes).
"""
from typing import Callable as Callable
from typing import Any as Any

class Pipe:
    """
    Represent a Pipeable Element :
    Described as :
    first = Pipe(lambda iterable: next(iter(iterable)))
    and used as :
    print [1, 2, 3] | first
    printing 1

    Or represent a Pipeable Function :
    It's a function returning a Pipe
    Described as :
    select = Pipe(lambda iterable, pred: (pred(x) for x in iterable))
    and used as :
    print [1, 2, 3] | select(lambda x: x * 2)
    # 2, 4, 6
    """

    def __init__(self, function: Callable[[Any], Any]) -> None: ...
    def __ror__(self, other: Any) -> Callable[[Any], Any]: ...
    def __call__(self, *args: Any, **kwargs: Any) -> "Pipe": ...
