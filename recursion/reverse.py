from typing import List, Tuple, Union


# e.g (1, (2, (3, None))) -> (3, (2, (1, None)))
def reverse(s List[Tuple[Union[int, None]]]):
    def f(s, r):
        if s is None:
            return None
        return f(s[1], (s[0], r))

    return f(s, None)
