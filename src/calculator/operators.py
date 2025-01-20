import math
from abc import (
    ABC,
    abstractmethod,
)
from decimal import Decimal


class IOperator(ABC):
    @abstractmethod
    def do_math(self, *operands: Decimal) -> Decimal:
        pass


class Plusovanie(IOperator):
    def do_math(self, *operands: Decimal) -> Decimal:
        return Decimal(sum(operands))


class Minusovanie(IOperator):
    def do_math(self, *operands: Decimal) -> Decimal:
        return operands[0] - sum(operands[1:])


class Umnozheniye(IOperator):
    def do_math(self, *operands: Decimal) -> Decimal:
        return Decimal(math.prod(operands))


class Delenie(IOperator):
    def do_math(self, *operands: Decimal) -> Decimal:
        if operands[0] == 0:
            return Decimal(0)
        if 0 in operands[1:]:
            raise ZeroDivisionError("На ноль делить нельзя.")
        return operands[0] / Decimal(math.prod(operands))


class Calculator:
    def __init__(self, operator: IOperator, *operands: int | float | str | Decimal) -> None:
        self.operator = operator
        self.operands = tuple(map(Decimal, operands))
        self.result = self.operator.do_math(*self.operands)

    def __str__(self) -> str:
        return str(self.result)


print(Calculator(Plusovanie(), 1, 2, 3))
