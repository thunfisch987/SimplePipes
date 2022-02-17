"""Module enabling a sh like infix syntax (using pipes).
"""
from typing import Callable, Any
import functools


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

    def __init__(self, function: Callable[[Any], Any]) -> None:
        self.function = function
        functools.update_wrapper(self, function)

    def __ror__(self, other: Any) -> Callable[[Any], Any]:
        return self.function(other)

    def __call__(self, *args: Any, **kwargs: Any) -> "Pipe":
        return Pipe(lambda x: self.function(x, *args, **kwargs))


if __name__ == "__main__":
    import doctest

    doctest.testfile("README.md")
