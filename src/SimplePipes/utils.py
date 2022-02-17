from SimplePipes.pipe import Pipe
from typing import Any, Iterable, Literal


@Pipe
def out(x: Any) -> Any:
    print(x)
    return x


@Pipe
def utf(x: str, encoding: Literal[8] | Literal[16] | Literal[32] = 8) -> bytes:
    if encoding in [8, 16, 32]:
        return x.encode(f"utf-{encoding}")
    raise ValueError("Unsupported encoding")


mkset = Pipe(set)
mkdict = Pipe(dict)
mklist = Pipe(list)
mktuple = Pipe(tuple)
