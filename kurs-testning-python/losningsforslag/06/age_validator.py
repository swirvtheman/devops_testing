# age_validator.py
def validate_age(age):
    if not isinstance(age, (int, float)):
        raise TypeError("Ålder måste vara ett tal")
    if age < 0 or age > 150:
        raise ValueError("Ålder måste vara mellan 0 och 150")
    if age <= 12:
        return "barn"
    elif age <= 17:
        return "ungdom"
    elif age <= 64:
        return "vuxen"
    else:
        return "senior"
