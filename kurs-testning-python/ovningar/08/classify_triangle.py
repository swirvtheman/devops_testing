def classify_triangle(a, b, c):
    """Klassificera en triangel baserat på sidlängderna."""
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("Sidlängder måste vara positiva")

    if a + b <= c or b + c <= a or a + c <= b:
        raise ValueError("Inte en giltig triangel")

    if a == b == c:
        return "liksidig"
    elif a == b or b == c or a == c:
        return "likbent"
    else:
        return "oliksidig"
