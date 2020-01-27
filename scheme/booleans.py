"""Boolean funcs."""


def _and(a, b):
    """Asks if expr `a` is True, if True returns the value of expr `b`, else False."""
    if a:
        return b

    return False


def _or(a, b):
    """Asks if expr `a` is True, if True returns True, else returns value of expr `b`."""
    if a:
        return a

    return b


def _land(a, b):
    """Lazy implementation of `_and`."""
    a = a()
    b = b()
    if a:
        return b

    return False

def _lor(a, b):
    """Lazy implementation of `_or`."""
    a = a()
    b = b()
    if a:
        return b

    return False
