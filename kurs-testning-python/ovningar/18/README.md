# Övning 18 - E-handel

I den här övningen kommer du få jobba med ett mer komplext scenario - en varukorg i en e-handel. Det här scenariot är mer likt det du kommer stöta på i verkligheten. Du har flera beteenden: lägga till varor, ta bort varor, beräkna totalsumma och tillämpa rabattkoder.

Det kommer bli fler scenarion och du kommer behöva använda `Scenario Outline` med `Examples`-tabeller.

I katalogen `ovning/18/ehandel/` finns de filer du behöver:

- `features/cart.feature` innehåller de scenarion som skall testas.
- `src/cart.py` innehåller Python-koden för varukorgen.
- `tests/test_cart.py` är filen du skall jobba med. Här ska du skriva alla step definitions som behövs. Använd övning 17 som referens.

Börja med att få de enklaste scenarierna att passera och jobba dig sedan framåt.

## Tips

- Använd `parsers.parse()` för att extrahera värden från Gherkin-stegen.
- Tänk på att priser är decimaltal så använd `float()` vid konvertering.
- `Scenario Outline` fungerar likadant som vanliga scenarion i pytest-bdd - varje rad i `Examples` blir ett eget testfall automatiskt.


