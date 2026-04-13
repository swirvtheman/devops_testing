# test_todo_pom.py
import pytest
from pages.todo_page import TodoPage


@pytest.fixture
def page(driver, live_server):
    """Skapa en TodoPage-instans."""
    return TodoPage(driver, live_server)


def test_heading_is_correct(page):
    page.navigate()
    assert page.get_heading() == "Mina uppgifter"


def test_add_single_todo(page):
    page.navigate()
    page.add_todo("Köp mjölk")
    assert "Köp mjölk" in page.get_todo_texts()


def test_add_multiple_todos(page):
    page.navigate()
    page.add_todo("Köp mjölk")
    page.add_todo("Städa köket")
    page.add_todo("Promenera hunden")
    assert len(page.get_todo_items()) == 3


def test_toggle_todo_done(page):
    page.navigate()
    page.add_todo("Testuppgift")
    page.toggle_todo(1)
    assert page.is_todo_done(1)


def test_delete_todo(page):
    page.navigate()
    page.add_todo("Radera mig")
    page.delete_todo(1)
    assert len(page.get_todo_items()) == 0


def test_counter_updates(page):
    page.navigate()
    page.add_todo("Uppgift 1")
    page.add_todo("Uppgift 2")
    assert "2 uppgifter" in page.get_count_text()

