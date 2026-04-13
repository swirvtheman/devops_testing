from calculator import Calculator

calc = Calculator()

result = calc.add(2, 3)
expected = 5
print(
    f"Test add: {'Passed' if result == expected else 'Failed'} | Expected: {expected} |Actual: {result}")

result = calc.subtract(5, 2)
expected = 3
print(
    f"Test subtract: {'Passed' if result == expected else 'Failed'} | Expected: {expected} |Actual: {result}")

result = calc.multiply(4, 3)
expected = 12
print(
    f"Test multiply: {'Passed' if result == expected else 'Failed'} | Expected: {expected} |Actual: {result}")

result = calc.divide(10, 0)
expected = 0
print(
    f"Test divide: {'Passed' if result == expected else 'Failed'} | Expected: {expected} |Actual: {result}")

result = calc.power(2, 3)
expected = 8
print(
    f"Test power: {'Passed' if result == expected else 'Failed'} | Expected: {expected} |Actual: {result}")

result = calc.sqrt(-1)
expected = 0
print(
    f"Test sqrt: {'Passed' if result == expected else 'Failed'} | Expected: {expected} |Actual: {result}")

result = calc.modulo(10, 0)
expected = 0
print(
    f"Test modulo: {'Passed' if result == expected else 'Failed'} | Expected: {expected} |Actual: {result}")
