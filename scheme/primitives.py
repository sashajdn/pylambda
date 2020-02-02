"""Base functions for scheme2python."""


import collections
import numbers


def car(l):
    """Returns the first element of a list of S-Expressions."""
    return l[0]


def cdr(l):
    """Returns all elements of a list except the first."""
    return l[1:]


def is_null(l):
    """Returns true if list is null, else returns false."""
    return len(l) == 0


def is_zero(a):
    """Returns true if number is zero, else false"""
    return a == 0


def is_number(a):
    """Returns true if `a` is a number else returns false."""
    return isinstance(a, numbers.Number)


def is_atom(a):
    """Checks if the item is an atom."""
    return not (isinstance(a, collections.abc.Sequence) and not isinstance(a, str))


def add1(n):
    """Adds one to n."""
    return n + 1


def sub1(n):
    """Subtracts one from n."""
    return n - 1


def is_lat(l):
    """Checks if the list `l` is flat and all elements are s-expressions."""
    if is_null(l):
        return True

    elif is_atom(car(l)):
        return is_lat(cdr(l))

    else:
        return False


def is_eq(a1, a2):
    """Returns true if `a1` is equal to `a2`."""
    return a1 == a2


def quote(_str=None):
    """Returns an empty list, or casted str of `_str` if param passed.

    NOTE: This is nothing more than synatic sugar to resemble schemes notation
    """
    if _str is None:
        return []

    return str(_str)


def cons(a1, a2):
    """Prepends `n` to `m`."""
    return [a1] + a2
