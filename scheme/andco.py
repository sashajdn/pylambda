"""Recursive functions with collectors."""


from base import cons, car, cdr, is_null, is_atom, quote
from numops import is_even
from operations import add, multiply


def evens_only_and_co(l, col):
    """Collects, evens, the multiplication of evens and addition of odds."""
    if is_null(l):
        return col(quote(), 1, 0)

    if is_atom(car(l)):
        if is_even(car(l)):
            return evens_only_and_co(cdr(l),
                                     lambda evens, p, s:
                                     col(cons(car(l), evens),
                                     multiply(car(l), p),
                                     s))

        else:
            return evens_only_and_co(cdr(l),
                                     lambda evens, p, s:
                                     col(evens,
                                     p,
                                     add(car(l), s)))

    else:
        return evens_only_and_co(car(l),
                                 lambda car_evens, carp, cars:
                                 evens_only_and_co(cdr(l),
                                                   lambda cdr_evens, cdrp, cdrs:
                                                   col(cons(car_evens, cdr_evens),
                                                       multiply(carp, cdrp),
                                                       add(cars, cdrs))))
