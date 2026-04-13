"""
Lösningsförslag för övning 13

- I filen conftest.py finns en fixture som heter 
  sample_book. Denna skapar en bok åt oss, utan 
  denna hade vi behövt använda client.post(...) 
  i toppen av varje test som behöver en bok. Notera 
  hur vi använder sample_book i uppgift 4, 6 och 7.

- Varje test har tre tydliga faser - förbered data, 
  utför anrop och verifiera resultat. Detta kallas 
  Arrange–Act–Assert, försök att identifiera dessa i testerna.
  
"""

""" 1. GET /api/books - tom lista som returnerar 200 och []"""
def test_empty_list_returns_200(client):
    response = client.get("/api/books")
    assert response.status_code == 200
    assert response.get_json() == []

""" 2. POST /api/books - skapa en bok, verifiera 201 och att boken har rätt fält"""
def test_create_book_returns_book_with_id(client):
    response = client.post("/api/books", json={
        "title": "Test-Driven Development",
        "author": "Kent Beck"
    })
    data = response.get_json()
    assert "id" in data
    assert isinstance(data["id"], int)
    assert data["title"] == "Test-Driven Development"
    assert data["author"] == "Kent Beck"

""" 3. POST /api/books - utan title skall du få 400"""
def test_create_book_without_title_returns_400(client):
    response = client.post("/api/books", json={
        "author": "Kent Beck"
    })
    assert response.status_code == 400
    assert "error" in response.get_json()

""" 4. GET /api/books/<id> - hämta skapad bok, skall ge 200 och rätt data"""
def test_get_existing_book(client, sample_book):
    book_id = sample_book["id"]
    response = client.get(f"/api/books/{book_id}")
    assert response.status_code == 200
    data = response.get_json()
    assert data["id"] == book_id
    assert data["title"] == "Clean Code"
    assert data["author"] == "Robert C. Martin"

""" 5. GET /api/books/999 - bok som inte finns, skall ge 404"""
def test_get_nonexistent_book_returns_404(client):
    response = client.get("/api/books/999")
    assert response.status_code == 404
    assert "error" in response.get_json()

""" 6. PUT /api/books/<id> - uppdatera titel, skall ge 200 och ny titel"""
def test_update_title(client, sample_book):
    book_id = sample_book["id"]
    response = client.put(f"/api/books/{book_id}", json={
        "title": "Clean Architecture"
    })
    assert response.status_code == 200
    data = response.get_json()
    assert data["title"] == "Clean Architecture"
    assert data["author"] == "Robert C. Martin"

""" 7. DELETE /api/books/<id> - radera bok, skall ge 200 och när du sedan försöker hämta den med GET skall du få 404"""
def test_delete_existing_book_returns_200(client, sample_book):
    book_id = sample_book["id"]
    response = client.delete(f"/api/books/{book_id}")
    assert response.status_code == 200

    # Försök hämta den raderade boken
    get_response = client.get(f"/api/books/{book_id}")
    assert get_response.status_code == 404
    assert "error" in get_response.get_json()

""" 8. Skapa tre böcker, verifiera att GET listar alla 3"""
def test_create_multiple_books_and_list(client):
    client.post("/api/books", json={
        "title": "Bok 1", "author": "Författare 1"
    })
    client.post("/api/books", json={
        "title": "Bok 2", "author": "Författare 2"
    })
    client.post("/api/books", json={
        "title": "Bok 3", "author": "Författare 3"
    })
    response = client.get("/api/books")
    data = response.get_json()
    assert response.status_code == 200
    assert len(data) >= 3
    titles = {book["title"] for book in data}
    assert "Bok 1" in titles
    assert "Bok 2" in titles
    assert "Bok 3" in titles
