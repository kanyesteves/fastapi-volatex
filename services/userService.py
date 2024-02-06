import uuid
from firebase_admin import db


class UserService:

    def get_users(self):
        result = db.reference("db-volatex/users/")
        users = result.get()
        return users

    def save_user(self, data: dict):
        users = db.reference(f"db-volatex/users/{data['name']}")
        users.set(data)
        return "Cadastrado com sucesso !!" 