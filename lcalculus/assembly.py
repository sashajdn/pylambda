"""Functional Assembly."""


# for visibility purposes only
add1 = lambda x: x + 1


def TRUE(x):
    return lambda y: x


def FALSE(x):
    return lambda y: y


def NOT(x):
    return x(FALSE)(TRUE)


def AND(x):
    lambda y: x(y)(x)


def OR(x):
    lambda y: x(x)(y)


def ZERO(f):
    return lambda x: x  # Same as FALSE


def ONE(f):
    return lambda x: f(x)


def TWO(f):
    return lambda x: f(f(x))


def THREE(f):
    return lambda x: f(f(f(x)))


def FOUR(f):
    return lambda x: f(f(f(f(x))))


def SUCC(n):
    return lambda f: lambda x: f(n(f)(x))


def ADD(a):
    return lambda b: b(SUCC)(a)


def MUL(a):
    return lambda b: lambda f: b(a(f))


def EXP(a):
    return lambda b: a(b)


def CONS(a):
    """Builds a tuple."""
    return lambda b: lambda s: s(a)(b)


def CAR(p):
    """Analogous to tuple[0]."""
    return p(TRUE)


def CDR(p):
    """Analogous to tuple[1]."""
    return p(FALSE)


def SUCCTUP(p):
    """Succ on a tuple.

    Eg:

    p = CONS(ONE)(ZERO)

    SUCCTUP(p) == CONS(TWO)(ONE)
    """
    return CONS(SUCC(CAR(p)))(CAR(p))


def BUILDSUCCTUP(a):
    """Builds a succesion tuple.

    Eg.

    SUCCTUP(ONE) -> s(TWO)(ONE)

    To get the first value, use the `TRUE` selector,
    and `FALSE` for the last value

    SUCCTUP(ONE)(TRUE) -> TWO
    SUCCTUP(ONE)(FALSE) -> ONE
    """
    return CONS(SUCC(a))(a)


def PRED(n):
    """Predecesor of n."""
    return CDR(n(SUCCTUP)(CONS(ZERO)(ZERO)))


def SUB(a):
    return lambda b: b(PRED)(a)


def ISZERO(n):
    return (n)(lambda f: FALSE)(TRUE)


def FACT(n):
    """Factorial. Duh!"""
    return ISZERO(n)(ONE)(MUL(n)(FACT(PRED(n))))


# Examples

print(SUCC(THREE)(add1)(0))  # 3 + 1

print(ADD(TWO)(THREE)(add1)(0))  # 2 + 3

print(MUL(TWO)(THREE)(add1)(0))  # 2 * 3

print(EXP(TWO)(THREE)(add1)(0))  # 2 ** 3


print(BUILDSUCCTUP(ONE)(TRUE)(add1)(0))  # 2
print(BUILDSUCCTUP(ONE)(FALSE)(add1)(0))  # 1

print(PRED(FOUR(THREE))(add1)(0))  # 80  (4 ** 3 - 1)

print(SUB(FOUR)(TWO)(add1)(0))  # 2

print(ISZERO(ZERO))  # TRUE
print(ISZERO(TWO))  # FALSE

print(FACT(ONE)(add1)(0))  # 1
print(FACT(FOUR)(add1)(0))  # 4 * 3 * 2 * 1 = 24  NOTE: recursion depth reached :(
