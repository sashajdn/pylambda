"""There are `6|six` types in scheme.

<Scheme>         : <Python Equivalent>
*const           : t_const
*quote           : t_quote
*indentifier     : t_indentifier
*lambda          : t_lambda
*cond            : t_cond
*application     : t_application

All represented via functions called `actions`

Primitive vs Non-Primitive functions:
  - We know what primitive functions do; Non-primitives we do
    not, they are defined by their arguments and function bodies.
"""


from primitives import  is_number, is_eq, quote, car, cdr, cons
from pairs import build
from tables import lookup_in_table


def initial_table(name):
    """Initial table helper func.

    NOTE: Should never get used.
    """
    return car(quote())


def table_of(exp):
    """Gets the table from t_lambda eval."""
    return car(cdr(first))


def formals_of(exp):
    """Gets the formals from t_lambda eval."""
    return car(cdr(cdr(exp)))


def body_of(exp):
    """Gets the body from t_lambda eval."""
    return car(cdr(cdr(cdr(exp))))


### --- TYPES --- ### 


def t_const(exp, table):
    """`t_const` type function: `*const` in schmeme."""
    if is_number(exp):
        return exp

    if is_eq(exp, quote("True")):
        return True

    if is_eq(exp, quote("False")):
        return False

    return build(quote("primitive", exp))


def t_quote(exp, table):
    """`t_quote` type function: `*quote` in schmeme."""
    return text_of(exp)


def t_identifier(exp, table):
    """`t_identifier` type function: `*identifier` in schmeme."""
    return lookup_in_table(exp, table, initial_table)


def t_lambda(exp, table):
    """`t_lambda` type function: `*lambda` in schmeme.

    Since for non-primitive functions, the args & func body
    need to be remembered, this is simply `cdr(exp)`
    """
    return build(quote("non-primitive"),
                 cons(table, cdr(exp)))

