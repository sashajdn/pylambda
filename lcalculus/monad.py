import functools
from typing import Callable, TypeVar


T = TypeVar('T')


class Number:
    def __init__(self, value: T):
        self.value = value

    def __rshift__(self, other: "Operation"):
        return Operation(functools.partial(other.operator, self.value))

    def __str__(self):
        return str(self.value)


class Operation:
    def __init__(self, operator: Callable[[T], T]):
        self.operator = operator

    def __rshift__(self, other: Number):
        return Number(self.operator(other.value))


# Example

Add = Operation(lambda x, y: x + y)  # type: ignore
Mul = Operation(lambda x, y: x * y)  # type: ignore

# (10 + 5) * 2
result = (Number(10) >> Add >> Number(5)) >> Mul >> Number(2)

print(result)  # 30
