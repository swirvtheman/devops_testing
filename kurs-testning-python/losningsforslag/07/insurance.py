# insurance.py
def calculate_premium(age: int, smoker: bool, bmi: float) -> int:
    base = 1000
    if age < 25:
        base += 500
    if smoker:
        base += 700
    if bmi > 30:
        base += 300
    return base

