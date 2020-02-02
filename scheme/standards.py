"""Standard funcs for `scheme2python`."""


from primitives import add1, car, cdr, cons, is_atom, is_null, is_zero, sub1, quote


### Lambda calc length: Note, python must have func defined so not quite (but closer)
## Use with the Y-combinator.
_LENGTH = lambda length: lambda l: 0 if is_null(l) else add1(length(cdr(l)))


def length(lat):
    """Returns the length of the lateral list `l`."""
    if is_null(lat):
        return 0

    else:
        return add1(length(cdr(lat)))


def pick(a, lat):
    """Pick function, returns the atom at position `a` for list `lat`."""
    if is_null(lat):
        return quote()

    elif is_zero(sub1(a)):
        return car(lat)

    else:
        return pick(sub1(a), cdr(lat))


def rempick(a, lat):
    """Remove the atom at position `a` from the list, `l`."""
    if is_null(lat):
        return quote()

    elif is_zero(sub1(a)):
        return (cdr(lat))

    else:
        return cons(car(lat),
                    rempick(sub1(a), cdr(lat)))


def leftmost(l):
    """Returns the leftmost atom from the list `l`."""
    if is_null(l):
        return quote()

    elif is_atom(car(l)):
        return car(l)

    else:
        return leftmost(car(l))
