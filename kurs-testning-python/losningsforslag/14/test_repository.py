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
    """ 1. get_all() på tom databas skall returnera en tom lista """
    assert repo.get_all() == []


def test_create_book_id_title_author(repo):
    """ 2. create() skall returnera en bok med id, titel och författare """
    book = repo.create("The Pragmatic Programmer", "Hunt & Thomas")
    assert book is not None
    assert "id" in book
    assert isinstance(book["id"], int)
    assert book["title"] == "The Pragmatic Programmer"
    assert book["author"] == "Hunt & Thomas"


def test_get_by_id_returns_correct_book(repo):
    """ 3. get_by_id() skall returnera rätt bok """
    book1 = repo.create("Book 1", "Author 1")
    book2 = repo.create("Book 2", "Author 2")
    book3 = repo.create("Book 3", "Author 3")

    retrieved_book = repo.get_by_id(book1["id"])
    assert retrieved_book is not None
    assert retrieved_book["id"] == book1["id"]
    assert retrieved_book["title"] == "Book 1"
    assert retrieved_book["author"] == "Author 1"

    retrieved_book = repo.get_by_id(book2["id"])
    assert retrieved_book is not None
    assert retrieved_book["id"] == book2["id"]
    assert retrieved_book["title"] == "Book 2"
    assert retrieved_book["author"] == "Author 2"

    retrieved_book = repo.get_by_id(book3["id"])
    assert retrieved_book is not None
    assert retrieved_book["id"] == book3["id"]
    assert retrieved_book["title"] == "Book 3"
    assert retrieved_book["author"] == "Author 3"


def test_get_by_id_invalid_id_returns_none(repo):
    """ 4. get_by_id() med ogiltigt id skall returnera None """
    assert repo.get_by_id(999) is None


def test_update_saves_changes(repo):
    """ 5. update() skall spara ändrad data """
    book = repo.create("Old Title", "Old Author")
    updated_book = repo.update(book["id"], "New Title", "New Author")
    assert updated_book is not None
    assert updated_book["title"] == "New Title"
    assert updated_book["author"] == "New Author"


def test_update_invalid_id_returns_none(repo):
    """ 6. update() med ogiltigt id skall returnera None """
    assert repo.update(999, "Title", "Author") is None


def test_delete_removes_book(repo):
    """ 7. Efter delete() skall boken inte finnas längre. """
    book = repo.create("Title", "Author")
    repo.delete(book["id"])
    assert repo.get_by_id(book["id"]) is None


def test_delete_invalid_id_returns_false(repo):
    """ 8. delete() med ogiltigt id skall returnera False """
    assert repo.delete(999) is False


def test_create_three_books_and_verify_order_and_count(repo):
    """ 9. Skapa tre böcker, verifiera ordning och antal. """
    book1 = repo.create("Book 1", "Author 1")
    book2 = repo.create("Book 2", "Author 2")
    book3 = repo.create("Book 3", "Author 3")
    all_books = repo.get_all()
    assert len(all_books) == 3
    assert all_books[0]["id"] == book1["id"]
    assert all_books[1]["id"] == book2["id"]
    assert all_books[2]["id"] == book3["id"]
