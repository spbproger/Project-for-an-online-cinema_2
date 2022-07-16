from dao.model.user import User


# CRUD - это набор операций: создание, чтение, обновление и удаление.
class UserDAO:
    """ДАО для модели пользователя."""
    def __init__(self, session):
        self.session = session

    def get_one(self, uid):
        """Метод получения инфы о пользователе по id."""
        return self.session.query(User).get(uid)

    def get_all(self):
        """Метод получения инфы о всех пользователях."""
        return self.session.query(User).all()

    def get_user_by_username(self, username: str):
        """Метод получения пользователя по имени (запрос:  /users/?username=Катерина )."""
        return self.session.query(User).filter(User.username == username).first()

    def get_by_role_user(self, role="user"):
        """Метод получения пользователя по его роли = user."""
        user_role = self.session.query(User).filter(User.role == role).all()
        for roles in user_role:
            if roles == "user":
                return roles
            return "Not Found", 404

    def get_by_role_admin(self, role="admin"):
        """Метод получения пользователя по его роли = admin."""
        admin_role = self.session.query(User).filter(User.role == role).all()
        for roles in admin_role:
            if roles == "admin":
                return roles
            return "Not Found", 404

    def create_user(self, user):
        """Метод создания нового пользователя в БД."""
        user_new = User(**user)
        self.session.add(user_new)
        self.session.commit()
        return user_new

    def delete(self, uid):
        """Метод удаления пользователя по id."""
        user = self.get_one(uid)
        self.session.delete(user)
        self.session.commit()

    def update(self, user_data):
        """Метод обновления инфы о пользователе."""
        user = self.get_one(user_data.get("id"))
        user.username = user_data.get("username")
        user.password = user_data.get("password")
        user.role_id = user_data.get("role_id")
        self.session.add(user)
        self.session.commit()
