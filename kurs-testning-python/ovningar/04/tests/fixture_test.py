from user_repository import UserRepository
from pathlib import Path
import sys

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))


@pytest.fixture
def repository_with_10_users():
    repo = UserRepository()
    for i in range(1, 11):
        user_id = f"user_{i}"
        repo.add_user(user_id, f"User {i}", f"user{i}@example.com")
    return repo


def test_create_10_users_with_fixture(repository_with_10_users):
    assert repository_with_10_users.count() == 10


@pytest.mark.parametrize("i", range(1, 11), ids=lambda i: f"user_{i}")
def test_each_created_user_has_expected_data(repository_with_10_users, i):
    user = repository_with_10_users.get_user(f"user_{i}")
    assert user["name"] == f"User {i}"
    assert user["email"] == f"user{i}@example.com"
