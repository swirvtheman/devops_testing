from hello import greet


def test_greet():
    assert greet("Anna") == "Hej, Anna!"


def test_greet_empty():
    assert greet("") == "Hej, !"
