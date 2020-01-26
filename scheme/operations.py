"""Operation functions for `scheme2python`."""


from primitives import add1, sub1, is_zero


def add(n, m):
    """Adds `n` and `m` together."""
    if is_zero(m):
        return n

    else:
        return add1(add(n, sub1(m)))


def sub(n, m):
    """Subs `m` from `n`."""
    if is_zero(m):
        return n

    else:
        return sub1(sub(n, sub1(m)))


def gt(n, m):
    """Returns true if `n` is greater than `m`."""
    if is_zero(n):
        return False

    elif is_zero(m):
        return True

    else:
        return gt(sub1(n), sub1(m))


def lt(n, m):
    """Returns true if `n` is less than `m`, otherwise returns false."""
    if is_zero(m):
        return False

    elif is_zero(n):
        return True

    else:
        return lt(sub1(n), sub1(m))


def multiply(n, m):
    """Multiplies `n` by `m`."""
    if is_zero(m):
        return 0

    else:
        return add(n, (multiply(n, sub1(m))))


def expon(n, m):
    """Raises `n` to the `m` power."""
    if is_zero(m):
        return 1

    else:
        return multiply(n, expon(n, sub1(m)))


def floor(n, m):
    """Floor divides `n` by `m`."""
    if lt(n, m):
        return 0

    else:
        return add1(floor(sub(n, m), m))


def eq_num(n, m):
    """Recursive function to check if `n` is equal to `m`."""
    if gt(n, m):
        return False

    elif lt(n, m):
        return False

    else:
        return True
