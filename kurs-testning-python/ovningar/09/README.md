# Övning 9 - Explorativ testning

## Uppdrag
Ni ska testa en Flask-app (TODO-lista) explorativt.

## Charter
*Utforska TODO-appens funktionalitet med fokus på att hitta buggar och oväntade beteenden.*

## Tidsbox: 30 minuter

## Dokumentera (i en textfil)
1. Vad testade jag?
2. Vilka buggar eller konstigheter hittade jag?
3. Vad hann jag inte testa?
4. Vilka risker ser jag?

## Starta appen

```sh
docker run -it --rm \  -v ./kurs-testning:/app -p 5000:5000 \  --name testlab \  ghcr.io/jonasbjork/testlab

cd ovningar/08/todo
python app.py
```

Om du inte använder containern måste du se till att Flask är installerat i Python. Annars fungerar inte appen.

Gå till http://localhost:5000 i webbläsaren, eller använd `curl` från terminalen.
