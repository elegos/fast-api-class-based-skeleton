from functools import reduce

from services.abc import MathABC, MathEquationBuilder

class Math(MathABC):
    def sum(self, *args) -> float:
        return reduce(lambda a, b: float(a) + float(b), args)

    def subtract(self, *args) -> float:
        return reduce(lambda a, b: float(a) - float(b), args[1:], float(args[1]))

    def divide(self, a, b) -> float:
        return float(a) / float(b)

    def multiply(self, a, b) -> float:
        return float(a) * b
    
    def builder(self) -> MathEquationBuilder:
        return MathEquationBuilder(self)
