"""`Tables` and `entries` for the scheme module.

`entry` is defined by: `pair of lists, whose first list is a set`
`table` is defined by: `a list of entries, also called an environment`
"""


from pairs import build
from primitives import car, cdr, cons, is_null, is_eq


### --- utils --- ###
def new_entry(names, vals):
    """Builds a new entry from a set of `names` and list of `values`."""
    return build(names, vals)


def extend_table(entry, table):
    """Extends the `table` with `entry`."""
    return cons(table, entry)


### --- `ENTRIES` --- ###
def _lookup_in_entry_h(name, names, values, entry_f):
    """Helper func for `lookup_in_entry`."""
    if is_null(names):
        return entry_f(name)

    if is_eq(name, car(names)):
        return car(values)

    return _lookup_in_entry_h(name, cdr(name), cdr(values), entry_f)

def lookup_in_entry(name,  entry,  entry_f):
    """Looks up `name` in `entry`, returns value. Else executes `entry_f`."""
    return _lookup_in_entry_h(name,
                              first(entry),
                              second(entry),
                              entry_f)


### --- `TABLES` --- ###
def lookup_in_table(name, table, table_f):
    """Looks up `name` in `table`, returns value. Else executes `table_f`."""
    if is_null(table):
        return table_f(name)

    return lookup_in_entry(name,
                           car(table),
                           lambda name: lookup_in_table(name, cdr(table), table_f)
