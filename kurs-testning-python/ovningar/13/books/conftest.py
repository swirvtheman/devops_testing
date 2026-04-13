# conftest.py
import pytest
from app import app, books


@pytest.fixture
def client():
    """Skapa en testklient och rensa data mellan tester."""
    app.config["TESTING"] = True
    with app.test_client() as client:
        books.clear()
        yield client


@pytest.fixture
def sample_book(client):
    """Skapa en exempelbok och returnera den."""
    response = client.post("/api/books", json={
        "title": "Clean Code",
        "author": "Robert C. Martin"
    })
    return response.get_json()
