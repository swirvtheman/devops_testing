# Övning 13 - Testa ett Flask REST-API

I Python har vi bra verkyg för integrationstestning. Flask har en inbyggd testklient som simulerar HTTP-anrop *utan* att starta en riktig server. Det gör testerna snabba, men ändå realistiska - hela request/response-cykeln körs genom Flask-applikationen.

```python
# Exempel: Flask testklient
def test_get_books(client):
    response = client.get("/api/books")
    assert response.status_code == 200
    assert isinstance(response.json, list)
```

Filerna hittar du i katalogen `ovningar/13/books/` .

## app.py

`app.py` är filen du skall testa. Det är ett enkelt REST-API för böcker. Just nu lagras böckerna i en vanlig lista i minnet - det byter vi ut mot en databas i nästa övning.

Lägg märke till att det finns validering: POST kräver `title` och `author`, och GET/PUT/DELETE returnerar 404 om boken inte finns. Det är sådant ni skall verifiera i era tester.

## conftest.py

Filen `conftest.py` är den viktigaste delen. Fixture `client` skapar en testklient och *rensar boklistan före varje test*. Det är kritiskt - varje test skall vara oberoende av andra tester.

Fixture `sample_book` bygger på `client`-fixturen och skapar en bok åt oss. Det slipper vi upprepa i varje test som behöver en bok att jobba med.

## Tester

Här är de testfall ni skall skriva, börja uppifrån och arbeta nedåt. Varje test skall vara en egen funktion - tänk på bra namngivning. Till exempel `test_get_books_empty_returns_empty_list` eller `test_create_book_missing_title_returns_400`.

Använd `sample_book`-fixturen där det är relevant, men för testet med den tomma listan (test 1) skall ni bara använda `client`.

1. `GET /api/books` - tom lista som returnerar `200` och `[]`
2. `POST /api/books` - skapa en bok, verifiera `201` och att boken har rätt fält
3. `POST /api/books` - utan `title` skall du få `400`
4. `GET /api/books/<id>` - hämta skapad bok, skall ge `200` och rätt data
5. `GET /api/books/999` - bok som inte finns, skall ge `404`
6. `PUT /api/books/<id>` - uppdatera titel, skall ge `200` och ny titel
7. `DELETE /api/books/<id>` - radera bok, skall ge `200` och när du sedan försöker hämta den med `GET` skall du få `404`
8. Skapa tre böcker, verifiera att `GET` listar alla 3.

## Tips

Starta Flask-applikationen i en terminal:

```sh
python app.py
```

Sedan startar du en ny terminal med containern, så du kan köra testerna:

```sh
docker exec -it <CONTAINER_ID> bash
```

### Hur skickar jag JSON-data?

`client.post("/url", json={...})`

### Hur läser jag svaret?

`response.get_json()` och `response.status_code`



