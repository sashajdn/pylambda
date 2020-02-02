"""Meta programming in the style of `scheme` in python. Apologies in advance."""


from primitives import is_atom, is_eq, is_number, quote


def atom_to_action(exp):
    """Converts an `exp` into an action, assuming `exp` is an `atom`."""
    if is_number(exp):
        return t_const
    if is_eq(exp, quote("#t"):
        return True
    if is_eq(exp, quote("#f"):
        return False
    if is_eq(exp, quote("cons")):
        return t_const
    if is_eq(exp, quote("car")):
        return t_const
    if is_eq(exp, quote("cdr")):
        return t_const
    if is_eq(exp, quote("null?")):
        return t_const
    if is_eq(exp, quote("eq?")):
        return t_const
    if is_eq(exp, quote("atom?")):
        return t_const
    if is_eq(exp, quote("zero?")):
        return t_const
    if is_eq(exp, quote("add1")):
        return t_const
    if is_eq(exp, quote("sub1")):
        return t_const
    if is_eq(exp, quote("number?")):
        return t_const

    return t_identifier


def list_to_action(exp):
    """Converts `exp` to `action, assuming `exp` is `list`."""
    if is_atom(car(e)):

        if is_eq(car(e), quote("quote")):
            return t_quote
        if is_eq(car(e), quote("lambda")):
            return t_lambda
        if is_eq(car(e), quote("cond")):
            return t_cond

        return t_application

    return t_application


def expression_to_action(exp):
    """Converts an `exp` to an action."""
    if is_atom(exp):
        return atom_to_action(exp)

    return list_to_action(exp)


def meaning(exp, table):
    """Determines the `meaning` of an expression, `exp`."""
    return expression_to_action(exp)(exp, table)


def value(exp):
    """Computes the value of the expresson, `exp`.

    NOTE: This can also be called the `interpreter`
    """
    return meaning(exp, quote())
