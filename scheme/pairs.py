"""`Pairs` for the scheme module.

`pair` is defined by: `A list of only two S-Expressions`
"""


from primitives import car, cdr, cons, quote, is_null, is_atom
from booleans import  _or


def is_pair(l):
    """Asks if `l` is in fact a `pair`."""
    if _or(is_atom(l), _or(is_null(l), is_null(car(l)))):
        return False

    if is_null(cdr(cdr(l))):
        return True

    return False


def first(pair):
    """Returns the first value of `pair`."""
    return car(pair)


def second(pair):
    """Returns the second value of`pair`."""
    return car(cdr(pair))


def build(s1, s2):
    """Builds a `pair` from two S-expressions: `s1`, `s2`."""
    return cons(s1, cons(s2, quote()))
