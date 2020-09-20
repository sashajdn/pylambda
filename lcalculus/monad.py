import abc
import functools
import operator as op
from typing import Callable, TypeVar, Union


T = TypeVar('T')


class INode(abc.ABC):
    @abc.abstractmethod
    def __call__(self):
        pass


class Number(INode):
    def __init__(self, value: T):
        self.value = value

    def __rshift__(self, other: "Operation"):
        return Operation(functools.partial(other.operator, self.value))

    def __str__(self):
        return str(self.value)

    def __call__(self):
        return self


class Operation(INode):
    def __init__(self, operator: Callable[[T], T]):
        self.operator = operator

    def __lshift__(self, other: Number):
        return Number(self.operator(other.value))

    def __rshift__(self, other: Number):
        return Number(self.operator(other.value))

    def __call__(self):
        return self.operator


class Expression(INode):
    def __init__(self, exp):
        self.exp = exp

    def __call__(self):
        return self.exp

    def __lshift__(self, other):
        return self.exp.__lshift__(other)

    def __rshift__(self, other):
        return self.exp.__rshift__(other)


class Graph(INode):
    def __init__(
        self,
        *,
        operator: Callable[[T], T],
        left: INode,
        right: INode,
    ):
        self.operator = operator
        self.left = left
        self.right = right

    def __call__(self):
        return self.left() >> self.operator << self.right()

    def __lshift__(self, other: Number):
        return Number(self.operator(other.value))

    def __rshift__(self, other: Number):
        return Number(self.operator(other.value))


Add = Operation(op.add)  # type: ignore
Mul = Operation(op.mul)  # type: ignore

e = Expression(
    Number(4) >> Mul << Number(6)
)

# operations or expressions
graph = Graph(
    operator=Add,  # type: ignore
    left=Graph(  # type: ignore
        operator=Mul,  # type: ignore
        left=Number(4),
        right=Number(10)
    ),
    right=Expression(
        Number(6) >> Add << Number(10)
    )
)

res = graph()
print(res)  # 56
