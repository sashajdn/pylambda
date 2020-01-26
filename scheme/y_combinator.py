"""Y Combinators."""

def Y(le):
    """Applicative order Y-Combinator func."""
    return (lambda f: f(f))(lambda f: le(lambda x: f(f)(x)))
