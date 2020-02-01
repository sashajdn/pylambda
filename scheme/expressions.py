"""Expressions for the `scheme` module.

DEFINTION: `<expression1> <operator> <expression2>
"""


from primitives import car, cdr, cons, is_eq
from operations import add, mutliply, expon


def _quote(atom):
    """Returns `str` of the `atom`."""
    return str(atom)

def first_sub_expr(aexp):
    """Returns the first sub expression from `aexp`."""
    return car(aexp)


def second_sub_expr(aexp):
    """Returns the second sub expression from `aexp`."""
    return car(cdr(cdr(aexp)))


def operator(nexp):
    """Returns the operator from `aexp`."""
    return car(cdr(aexp))


def value(nexp, fse, sse, op):
    """Executes the `nexp` and returns the value.

    Whereby:
    fse: first_sub_expr
    sse: second_sub_expr
    op: operator
    """
    def _value(nexp):
        if is_eq(op(nexp), _quote("+")):
            return add(_value(fse(nexp)),
                       (_value(sse(nexp))))

        if is_eq(op(nexp), _quote("x")):
            return multiply(_value(fse(nexp)),
                            (_value(sse(nexp))))

        return expon(_value(fse(nexp)),
                     (_value(sse(nexp))))

    return _value(nexp)
