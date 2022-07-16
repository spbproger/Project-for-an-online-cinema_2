import base64
import hashlib
import hmac
from helpers.constants import PWD_HASH_SALT, PWD_HASH_ITERATIONS
from dao.user import UserDAO


class UserService:
    """Класс бизнес-логики: пользователь."""
    def __init__(self, dao: UserDAO):
        self.dao = dao

    def get_one(self, uid):
        """Метод получения одного пользователя по его ID."""
        return self.dao.get_one(uid)

    def get_all(self):
        """Метод получения инфы о всех пользователях ( /users/ ).
        - по имени ( /users/?username=Олег ).
        - по роли ( /users/?role=user )."""
        return self.dao.get_all()

    def get_user_by_username(self, username):
        """Метод получения инфы о пользователей по имени  ( /users/?username=Ольга )."""
        return self.dao.get_user_by_username(username)

    def get_by_role_user(self, role):
        """Метод получения пользователей с ролью user."""
        return self.dao.get_by_role_user(role)

    def get_by_role_admin(self, role):
        """Метод получения пользователей с ролью admin."""
        return self.dao.get_by_role_admin(role)

    def get_hash(self, password):
        """Метод генерации хеша пароля пользователя."""
        return base64.b64encode(hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),
            PWD_HASH_SALT,
            PWD_HASH_ITERATIONS
        ))

    def compare_passwords(self, password_hash, other_password):
        """Метод сравнения хэша паролей."""
        return hmac.compare_digest(
            base64.b64decode(password_hash),
            hashlib.pbkdf2_hmac(
                'sha256',
                other_password.encode('utf-8'),  # Преобразовываем пароль в байты
                PWD_HASH_SALT,
                PWD_HASH_ITERATIONS
            ))

    def create_user(self, user):
        """Метод создания нового пользователя."""
        user['password'] = self.get_hash(user['password'])
        return self.dao.create_user(user)

    def update(self, user_data):
        """Метод обновления одного пользователя."""
        user_data["password"] = self.get_hash(user_data.get("password"))
        self.dao.update(user_data)
        return self.dao

    def delete(self, uid):
        """Метод удаления пользователя по id."""
        self.dao.delete(uid)
