# calculator.py

class Calculator:
    """En enkel miniräknare."""

    def add(self, a: float, b: float) -> float:
        return a + b

    def subtract(self, a: float, b: float) -> float:
        return a - b

    def multiply(self, a: float, b: float) -> float:
        return a * b

    def divide(self, a: float, b: float) -> float:
        if b == 0:
            raise ValueError("Kan inte dividera med noll")
        return a / b

    def power(self, a: float, b: float) -> float:
        return a ** b
