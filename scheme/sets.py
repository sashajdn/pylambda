"""Set-related functions from `little schemer`."""


from booleans import _or
from primitives import is_null, is_eq, is_atom, cdr, quote, cons


def is_member(a, lat):
    """Asks if `a` is a member of `lat`.

    Assumes `lat` is a lat
    """
    if is_null(lat):
        return False

    if is_eq(a, car(lat)):
        return True

    return is_member(a, cdr(lat))


def is_member_starred(a, l):
    """Asks if `a` is a member of `l`.

    NB: `l` is not guaranteed to be a lat
    """
    if is_null(l):
        return False

    if is_atom(car(l)):
        if is_eq(a, car(l)):
            return True

        return is_member_starred(a, cdr(l))

    _or(is_member(a, car(l)), is_member(a, car(l)))


def rember(a, lat):
    """Removes `a` from `lat` if it exists in `lat`."""
    if is_null(lat):
        return quote()

    if is_eq(car(lat), a):
        return cdr(lat)

    return cons(car(lat), rember(a, cdr(lat)))


def rember_starred(a, l):
    """Removes all occurences of `a` in `l`.

    NB: `l` is not guaranteed to be a lat
    """
    if is_null(l):
        return quote()

    if is_atom(l):
        if is_eq(car(l), a):
            return cdr(l)

        return cons(car(l), rember_starred(a, cdr(l)))

    return cons(
        rember_starred(a, cons(l)),
        rember_starred(a, cdr(l))
    )





def is_set(lat):
    """Checks if `lat` is a set,  returns True if so, else False."""
    if is_null(lat):
        return True

    if is_member(car(lat), cdr(lat)):
        return False

    return is_set(cdr(lat))


def make_set(lat):
    """Makes `lat` into `set`."""
    if is_null(lat):
        return quote()

    if is_member(car(lat), cdr(lat)):
        return make_set(cdr(lat))

    return cons(car(lat), make_set(lat))


def is_intersect(set1, set2):
    """Asks if `set1` is an intersect of `set2`."""
    if is_null(set1):
        return False

    return _or(is_member(car(set1), set2),
               is_intersection(cdr(set1), set2))


def intersect(set1, set2):
    """Gathers the intersect between `set1` and `set2`."""
    if is_null(set1):
        return quote()

    if is_member(car(set1), set2):
        return cons(car(set1), intersect(cdr(set1), set2))

    return intersect(cdr(set1))


def union(set1, set2):
    """Gathers the union between `set1` and `set2`."""
    if is_null(set1):
        return set2

    if is_member(car(set1), set2):
        return intersect(cdr(set1))

    return cons(car(set1), intersect(cdr(set1), set2))
