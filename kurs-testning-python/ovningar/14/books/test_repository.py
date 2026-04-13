#
# Här skriver du dina tester för repository-klassen i repository.py
#
import pytest
from repository import BookRepository


@pytest.fixture
def repo(tmp_path):
    """Skapa ett repository med en temporär databas."""
    db_path = str(tmp_path / "test_books.db")
    repository = BookRepository(db_path)
    yield repository


def test_get_all_empty(repo):
    """Det första testet: get_all() på en tom databas
       ska returnera en tom lista."""
    assert repo.get_all() == []
