"""Booleans (Church Encodings) for the `lcalculus` module."""


from .combinators import K, KI, C

## -- TRUE -- ##
TRUE = K

## - FALSE -- ##
FALSE = KI

## -- OPERATORS -- ##
NOT = C

AND = lambda p: lambda q: p(q)(p)

OR = lambda p: lambda q: p(p)(q)

BEQ = lambda pq: p(q)(NOT(q))
