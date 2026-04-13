# Övning 1 - Sätt upp labbmiljön

## Komma igång

Du kommer kunna använda vilken utvecklingsmiljö du vill: Visual Studio Code, PyCharm, vim, Emacs, ... 
Hela kursen bygger på att vi använder en containerimage som innehåller allt vi kommer behöva använda. 
Du behöver ha [Docker Desktop](https://www.docker.com/products/docker-desktop/) eller [Podman Desktop](https://podman-desktop.io) installerat, 
båda finns för Linux, macOS och Windows och fungerar för alla.

1. Se till att Docker Desktop eller Podman Desktop är installerat och fungerar.
2. Skapa en katalog där du kommer ha dina filer, säg `projekt`.
3. Bygg eller hämta hem containerimagen `testing`, instruktioner [finns här](../container/README.md).

## Tips

1. Öppna din `projekt/` katalog i din utvecklingsmiljö (VS Code, PyCharm, ..) och installera stöd för Python i den (extensions).
2. När du startat upp en instans av containern testing kan du öppna en annan terminal och köra kommandon mot den, som `docker exec testlab pytest` utan att vara inne i containern.
3. Allt du sparar i din `projekt/`-katalog dyker upp i katalogen `/app` inne i containern.

## Hello Test

Skapa två filer: `hello.py` och `test_hello.py`:

```python
# hello.py
def greet(name):
    return f"Hej, {name}!"
```

```python
# test_hello.py
from hello import greet

def test_greet():
    assert greet("Anna") == "Hej, Anna!"

def test_greet_empty():
    assert greet("") == "Hej, !"
```

Starta sedan containern och kör kommandot `pytest` inne i containern för att se att båda testerna passerar.
