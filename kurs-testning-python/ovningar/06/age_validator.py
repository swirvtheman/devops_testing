def validate_age(age):
    """Return age group for valid ages and raise ValueError for invalid input."""
    if not isinstance(age, int):
        raise ValueError("age must be an integer")

    if age < 0 or age > 150:
        raise ValueError("age must be between 0 and 150")

    if age <= 12:
        return "barn"
    if age <= 17:
        return "ungdom"
    if age <= 64:
        return "vuxen"
    return "senior"
