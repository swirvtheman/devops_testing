class AuthService:
    def __init__(self):
        self.users = {}

    def register(self, username, password):
        self.users[username] = password

    def login(self, username, password):
        if username not in self.users:
            return {"success": False, "error": "Användaren finns inte"}
        if self.users[username] != password:
            return {"success": False, "error": "Felaktigt lösenord"}
        return {"success": True, "error": None}
