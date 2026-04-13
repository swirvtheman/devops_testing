# user_repository.py

class UserRepository:
    def __init__(self):
        self.users = {}

    def add_user(self, user_id: str, name: str, email: str):
        if user_id in self.users:
            raise ValueError(f"Användare {user_id} finns redan")
        self.users[user_id] = {"name": name, "email": email}

    def get_user(self, user_id: str) -> dict:
        if user_id not in self.users:
            raise KeyError(f"Användare {user_id} hittades inte")
        return self.users[user_id]

    def delete_user(self, user_id: str):
        if user_id not in self.users:
            raise KeyError(f"Användare {user_id} hittades inte")
        del self.users[user_id]

    def count(self) -> int:
        return len(self.users)
