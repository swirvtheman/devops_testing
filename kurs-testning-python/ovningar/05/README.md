# Övning 5 - Coverage

Här skall du använda din calculator.py och test_calculator.py från övning 4.

1. Kör:

```sh
pytest --cov=calculator --cov-branch --cov-report=term-missing test_calculator.py
```

2. Analysera vilka rader och branches som saknar täckning.
3. Skriv tester tills ni når 100% branch coverage
4. Flaggan `--cov-report=term-missing` visar exakt vilka rader som missas


- Det vanligaste som missas är felhantering - exceptions, edge cases och if-satser. Kontrollera era if-satser noggrant!
- `term-missing` visar radnummer som saknar täckning, t.ex. `Missing: 3-6, 14`
- `BrPart` (Branch Partial) betyder att en branch bara testas i ena riktningen.

## Om du blir klar snabbt

- Utöka `Calculator` med en ny metod - `power(a, b)` eller `modulo(a, b)` och skriv tester som ger 100% coverage direkt.



