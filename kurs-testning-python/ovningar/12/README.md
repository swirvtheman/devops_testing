# Övning 12 - Mocka externa beroenden

Er uppgift är att skriva tester utan att göra riktiga nätverksanrop. Ni skall använda responses-biblioteket som vi gick igenom.

## Grundläggande tester

1. `get_temperature` returnerar korrekt temperatur
2. `get_forecast` returnerar prognoslista
3. Korrekt URL och parametrar skickas

## Felhantering (testa)

1. API returnerar HTTP 404 -> testa att exception kastas
2. API returnerar HTTP 500 -> testa exception
3. API returnerar ogiltig JSON (`KeyError`)
4. Nätverksfel (`ConnectionError`)

## Bonusuppgifter

1. Timeout-scenario
2. Testa att `api_key` skickas korrekt som parameter
3. Mocka med `pytest-mock` istället för responses

## Tips

- Använd responses-biblioteket (`@responses.activate`)
- `responses.add()` för varje scenario
- `pytest.raises()` för felhantering

