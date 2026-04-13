# calculator.py
class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            # Avsiktlig bugg: returnerar sträng istället
            # för att kasta exception
            return "Error"
        return a / b

    def power(self, base, exp):
        return base ** exp

    def sqrt(self, a):
        if a < 0:
            return "Error"
        return a ** 0.5

    def modulo(self, a, b):
        return a % b  # Bugg: hanterar inte b == 0
