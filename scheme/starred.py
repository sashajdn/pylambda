"""Starred (*) functions."""


from base import add1, is_eq, is_null, is_atom, car, cdr, cons, quote
from operations import add


def occur_starred(a, l):
    """Returns the the number of occurrences of `a` in `l`."""
    if is_null(l):
        return 0

    elif is_atom(car(l)):

        if is_eq(car(l), a):
            return add1(occur_starred(a, cdr(l)))

        else:
            return occur_starred(a, cdr(l))

    else:
        return add(occur_starred(a, car(l)), occur_starred(a, cdr(l)))


def insertR_starred(new, old, l):
    """Inserts `new` to the right of `old`, if `old` found in `l` for every occurrence."""
    if is_null(l):
        return quote()

    elif is_atom(car(l)):

        if is_eq(car(l), old):
            return cons(old, cons(new, insertR_starred(new, old, cdr(l))))

        else:
            return cons(car(l), insertR_starred(new, old, cdr(l)))

    else:
        return cons(insertR_starred(new, old, car(l)),
                    insertR_starred(new, old, cdr(l)))


def insertR_starred(new, old, l):
    """Inserts `new` to the left of `old`, if `old` found in `l` for every occurrence."""
    if is_null(l):
        return quote()

    elif is_atom(car(l)):

        if is_eq(car(l), old):
            return cons(new, cons(old, insertR_starred(new, old, cdr(l))))

        else:
            return cons(car(l), insertR_starred(new, old, cdr(l)))

    else:
        return cons(insertR_starred(new, old, car(l)),
                    insertR_starred(new, old, cdr(l)))
