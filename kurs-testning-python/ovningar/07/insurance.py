def calculate_premium(age, is_smoker, bmi):
    """Calculate monthly insurance premium based on age, smoking, and BMI."""
    premium = 1000

    if age < 25:
        premium += 500

    if is_smoker:
        premium += 700

    if bmi > 30:
        premium += 300

    return premium
