# Övning 14 - Databasintegration

Här skall vi testa att vår pythonkod och databas fungerar ihop. Vi verifierar SQL-frågor och att data sparas korrekt, och att edge cases hanteras.

Filerna finns i katalogen `ovningar/14/books`.

## Repository-klassen

Repositoryt finns i filen `repository.py`. Det är ett lager över SQLite databasen som hanterar CRUD-operationer och returnerar dictionaries. Inget märkvärdigt, men det är just sådana här gränssnitt som behöver integrationstester.

Poängen är att vi *inte* mockar databasen. Vi kör mot en riktig SQLite-fil. Det gör att vi fångar upp SQL-buggar och datatyps-problem som enhetstester med mockar aldrig skulle hitta.

Test-fixturen med temporär databas hittar vi i filen `test_repository.py` :

```python
import pytest
import os
from repository import BookRepository

@pytest.fixture
def repo(tmp_path):
    """Skapa ett repository med en temporär databas."""
    db_path = str(tmp_path / "test_books.db")
    repository = BookRepository(db_path)
    yield repository
```

`tmp_path` är en inbyggd pytest-fixture som ger oss en unik temporär katalog för varje test. Vi skapar databasen där och pytest städar upp allt när vi är klara.

Det betyder att varje test får en ny, *fräsch*, tom databas. Inget läckage mellan tester. Att varje test sätter upp sin egen databas är standard för bra integrationstester.

## Testning

Implementera tester för:

1. `get_all()` på tom databas skall returnera en tom lista
2. `create()` skall returnera en bok med id, titel och författare
3. `get_by_id()` skall returnera rätt bok
4. `get_by_id()` med ogiltigt id skall returnera `None`
5. `update()` skall spara ändrad data
6. `update()` med ogiltigt id skall returnera `None`
7. Efter `delete()` skall boken inte finnas längre.
8. `delete()` med ogiltigt id skall returnera `False`
9. Skapa tre böcker, verifiera ordning och antal.

Mönstret är det samma som i övning 13, men nu testar vi direkt mot repositoryt och databasen - utan Flask. Tänk på att varje test skall vara oberoende - `repo`-fixturen ger dig en tom databas varje gång, därför behöver du skapa en bok i testets början om du vill kunna arbeta med den boken senare i testet.

```python
def test_create_book(repo):
    book = repo.create("The Pragmatic Programmer", "Hunt & Thomas")
    assert book["title"] == "The Pragmatic Programmer"
    assert book["author"] == "Hunt & Thomas"
    assert "id" in book

def test_get_nonexistent_book(repo):
    assert repo.get_by_id(999) is None
```

