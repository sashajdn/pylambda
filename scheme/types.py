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


from meta import meaning
from pairs import build, first
from primitives import  is_number, is_eq, quote, car, cdr, cons, is_atom
from tables import lookup_in_table, new_entry, extend_table


### --- utils --- ###
def initial_table(name):
    """Initial table helper func.

    NOTE: Should never get used.
    """
    return car(quote())


### --- *lambda utils --- ###
def table_of(exp):
    """Gets the table from t_lambda eval."""
    return car(cdr(first))


def formals_of(exp):
    """Gets the formals from t_lambda eval."""
    return car(cdr(cdr(exp)))


def body_of(exp):
    """Gets the body from t_lambda eval."""
    return car(cdr(cdr(cdr(exp))))


### ---  *cond utils --- ###
def is_else(x):
    """Asks if `x` is an else statement."""
    if is_atom(x):
        return is_eq(x, quote("else"))

    return False


def question_of(line):
    """Gets the question from a line.

    Example: ((null? x) (quote('else'))
    Here would return (null? x), as this is the `car` of the list
    """
    return car(line)


def answer_of(line):
    """Gets the answer of the line, if the question is Truthy."""
    return car(cdr(line))


def evcon(lines, table):
    """Helper to evaluate `cond` lines."""
    if is_else(question_of(car(lines))):
        return meaning(exp=answer_of(car(lines)), table=table)

    if meaning(exp=uestion_of(car(lines)), table=table):
        return meaning(exp=answer_of(car(lines)), table=table)

    return evcon(cdr(lines), table)


def cond_lines_of(lines):
    """Retrieves only the `cond` lines in exp."""
    if is_eq(car(car(lines)), quote("cond")):
        return cdr(lines)

    return cond_lines_of(cdr(lines))


### --- *application utils --- ###
def function_of(exp):
    """Returns the function of an application."""
    return car(cdr(exp))


def arguments_of(exp):
    """Returns the arguments of the function an application."""
    return car(cdr(cdr(exp)))


def is_primitive(l):
    """Asks the question if `l` is a primitive."""
    return is_eq(first(l), quote("primitive"))


def is_non_primitive(l):
    """Asks the question if `l` is a primitive."""
    return is_eq(first(l), quote("non-primitive"))


def evlis(args, table):
    """This returns a list composed of the meaning of each argument."""
    if is_null(args):
        return quote()

    return cons(exp=meaning(car(args), table=table),
                evlis(args=cdr(args), table=table))


def _is_atom(x):
    """Asks if atom, checks for primitives and non-primitives as well."""
    if is_atom(x): return True
    if is_null(x): return False
    if is_eq(car(x), quote("primitive")): return True
    if is_eq(car(x), quote("non-primitive")): return True
    return False


def apply_primitive(name, vals):
    """Applies the primitive function `name`, with args=`vals`."""
    if is_eq(name, quote("cons")):
        return cons(first(vals), second(vals))

    if is_eq(name, quote("car")):
        return car(first(vals))

    if is_eq(name, quote("cdr")):
        return cdr(first(vals))

    if is_eq(name, quote("null?")):
        return is_null(first(vals))

    if is_eq(name, quote("eq?")):
        return is_eq(first(vals), second(vals))

    if is_eq(name, quote("atom?")):
        return _is_atom(first(vals))

    if is_eq(name, quote("zero?")):
        return is_zero(first(vals))

    if is_eq(name, quote("add1")):
        return add1(first(vals))

    if is_eq(name, quote("sub1")):
        return sub1(first(vals))

    if is_eq(name, quote("number?")):
        return is_number(first(vals))


def apply_closure(closure, vals):
    """Applies a given closure, by finding `meaning` of the body & extending the table."""
    return meaning(exp=body_of(closure),
                   table=extend_table(
                       new_entry(formals_of(closure), vals),
                       table_of(closure)
                   ))


def apply(fun, vals):
    """Apply the `fun` with the arguments `vals`."""
    if is_primitive(fun):
        return apply_primitive(second(fun), vals)

    return apply_closure(second(fun), vals)


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


def t_cond(exp, table):
    """`t_cond` type function: `*cond in scheme`.

    `cond` takes in any number of `cond`-lines. It considers each line
    in turn. If the question on the left is Falsey, it looks at the
    rest of the lines.
    Otherwise it proceeds to answer th  right part. If it sees an
    `else`-line,  it treats that line as if it was Truthy
    """
    return evcon(cond_lines_of(exp), table))


def t_application(exp, table):
    """`t_application` type function: `*application in scheme`.

    An application is a list of expressions whose `car` position
    contains an expression, whoses value is a funciton.

    An application must always determine the meaning of all it's
    arguments. This is what differs it from say `cond`, `or`, `and`

    NB: Only two types of funcs: primitive & non-primitive
    """
    return apply(meaning(exp=function_of(exp), table=table),
                 evlis(arguments_of(exp), table))
