"""Recursive functions with collectors

NB: <>&co functions in little-schemer.
"""


from primitives import cons, car, cdr, is_null, is_atom, quote, is_eq
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


def multiinsertLR_starred_and_co(new, oldL, oldR, l, col):
    """Inserts new to the left of `oldL` and to the right of `oldR`.

    NB: Uses a collector func to gather new list and count L, R inserts
    """
    if is_null(l):
        return col(quote(), 0, 0)

    elif is_atom(car(l)):
        if is_eq(car(l), oldL):
            return multiinsertLR_starred_and_co(new, oldL, oldR, cdr(l),
                                                lambda newl, L, R:
                                                col(cons(new, cons(oldL, newl)),
                                                    add1(L),
                                                    R))
        elif is_eq(car(l), oldR):
            return multiinsertLR_starred_and_co(new, oldL, oldR, cdr(l),
                                                lambda newl, L, R:
                                                col(cons(oldR, cons(new, newl)),
                                                    L,
                                                    add1(R)))

        else:
            return multiinsertLR_starred_and_co(new, oldL, oldR, cdr(l),
                                                lambda newl, L, R:
                                                col(cons(car(l), newl),
                                                    L,
                                                    R))
    else:
        return multiinsertLR_starred_and_co(new, oldL, oldR, car(l),
                                            lambda carnl, carL, carR:
                                            multiinsertLR_starred_and_co(new, oldL, oldR, cdr(l),
                                                                         lambda cdrnl,  cdrL, cdrR:
                                                                         col(cons(carnl, cdrnl),
                                                                             add(carL, cdrL),
                                                                             add(carR, cdrR))))
