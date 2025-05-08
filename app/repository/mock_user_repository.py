from app.interfaces.user_repository import IUserRepository

class MockUserRepository(IUserRepository):
    def __init__(self):
        self.users = {}

    def create_user(self, user_id, user_data):
        if user_id in self.users:
            raise ValueError("User already exists")
        self.users[user_id] = user_data
        return user_data

    def get_user(self, user_id):
        return self.users.get(user_id)

    def update_user(self, user_id, user_data):
        if user_id not in self.users:
            raise ValueError("User not found")
        self.users[user_id].update(user_data)
        return self.users[user_id]

    def delete_user(self, user_id):
        if user_id not in self.users:
            raise ValueError("User not found")
        del self.users[user_id]