"""Parsing funcs for `scheme2python`."""


from primitives import car, cdr, cons, is_atom, is_number, is_null, quote


def no_nums(l):
    """Remove all the numbers in the list `l`."""
    if is_null(l):
        return quote()

    elif is_atom(car(l)):
        if is_number(car(l)):
            return no_nums(cdr(l))

        else:
            return cons(car(l), (no_nums(cdr(l))))

    else:
        return cons(no_nums(car(l)),
                    no_nums(cdr(l)))


def all_nums(l):
    """Return all numbers from list `l`."""
    if is_null(l):
        return quote()

    elif is_atom(car(l)):

        if is_number(car(l)):
            return cons(car(l), all_nums(cdr(l)))

        else:
            return all_nums(cdr(l))

    else:
        return cons(all_nums(car(l)),
                    all_nums(cdr(l)))
