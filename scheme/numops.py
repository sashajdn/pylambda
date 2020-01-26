"""Numbers."""


from primitives import add, sub, multiply, floor, eq_num


def is_even(n):
    """Returns True if n is even, else False."""
    return eq_num(multiply(floor(n, 2), 2), n)
