"""Combinators as defined by `R. Smullyan` with bird metaphors."""


## -- IDIOT -- ##
I = lambda f:f


## -- MOCKINGBIRD -- ##
M = lambda f: f(f)


## -- KESTREL -- ##
K = lambda a: lambda b: a


## -- CARDINAL -- ##
C = lambda f: lambda a: lambda b: f(b)(a)


## -- KITE -- ##
KI = C(K)
