# SimplePipes: Infix programming toolkit

Module enabling a sh like infix syntax (using pipes).

> Fork of JulienPalard/Pipe  
> Changes: from pipe import \* only imports the Pipe class / decorator  
> helper functions available in SimplePipes.utils
> (see: [Existing Pipes](<#existing-pipes-simplepipesutils>))

## Syntax

The basic syntax is to use a Pipe like in a shell:

```python
>>> [1, 2, 3] | makeset
{1, 2, 3}
```

## Constructing your own

You can construct your pipes using Pipe class initialized with lambdas like:

```python
from SimplePipes import Pipe
stdout = Pipe(lambda x: sys.stdout.write(str(x)))
select = Pipe(lambda iterable, pred: (pred(x) for x in iterable))
```

Or using decorators:

```python
from SimplePipes import Pipe
@Pipe
def stdout(x):
    sys.stdout.write(str(x))
```

## Existing Pipes (SimplePipes.utils)

List of available pipes; when several names are listed for a given pipe, these are aliases.

```python
| out
    @Pipe
    def out(x: Any) -> Any:
        print(x)
        return x
    -> # prints the value and returns it

    Example:
    >>> "Hello World" | out
    # Output: Hello World
    >>> test = "Hello World" | out
    >>> print(test)
    # Output: Hello World
    # Output: Hello World

| utf8
    @Pipe
    def utf8(x: str, encoding: int = 8) -> bytes:
        return x.encode(f"utf-{encoding}")
    -> # encrypts the given string
        # the encoding options defaults to 8 and can be 8, 16 or 32

    Example:
    >>> "Hello World" | utf
    # Output: b"Hello World"
    >>> "Hello World" | utf(16)
    # Output: b"\xff\xfey\x00e\x00e\x00t\x00" [encoded with utf-16]

| mkset
    mkset = Pipe(set)
    -> # makes a set from the given input

    Example:
    >>>[1, 2, 3] | makeset
    # Output: {1, 2, 3}

| mkdict
    mkdict = Pipe(dict)
    -> #makes a dictionary from the given input

    Example:
    >>> | mkdict
    # Output: {}

| mklist
    mklist = Pipe(dict)
    -> #makes a list from the given input

    Example:
    >>>{1, 2, 3} | mklist
    # Output: [1, 2, 3]

| mktuple
    mktuple = Pipe(tuple)
    -> #makes a tuple from the given input

    Example:
    >>>[1, 2, 3] | mktuple
    # Output: {1, 2, 3}
```
