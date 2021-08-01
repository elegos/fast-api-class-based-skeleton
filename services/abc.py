from abc import ABC, abstractmethod

class MathABC(ABC):
    @abstractmethod
    def sum(*args) -> float:
        pass

    @abstractmethod
    def subtract(*args) -> float:
        pass

    @abstractmethod
    def divide(a, b) -> float:
        pass

    @abstractmethod
    def multiply(a, b) -> float:
        pass

    def builder() -> 'MathEquationBuilder':
        pass


class MathEquationBuilder:
    mathLib: MathABC
    result: float

    def __init__(self, mathLib: MathABC):
        self.mathLib = mathLib
        self.result = 0.0 

    def sum(self, *args) -> 'MathEquationBuilder':
        self.result = self.mathLib.sum(self.result, *args)

        return self

    def subtract(self, *args) -> 'MathEquationBuilder':
        self.result = self.mathLib.subtract(self.result, *args)

        return self

    def divide(self, a) -> 'MathEquationBuilder':
        self.result = self.mathLib.divide(self.result, a)
        return self

    def multiply(self, a) -> 'MathEquationBuilder':
        self.result = self.mathLib.multiply(self.result, a)

        return self
    
    def build(self) -> float:
        return self.result
