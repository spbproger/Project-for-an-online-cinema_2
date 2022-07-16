from flask import request
from flask_restx import Resource, Namespace

from dao.model.user import UserSchema
from helpers.decorators import admin_required, auth_required
from implemented import user_service

user_ns = Namespace('users')

"""Представления сущности пользователи /users/."""
@user_ns.route('/')
class UsersView(Resource):
    def get(self):
        """Метод для получения инфы о всех пользователях
        - по имени /users/?username=Олег.
        - по роли /users/?role=user."""
        username = request.args.get("username")
        admin = request.args.get("admin")
        user = request.args.get("user")

        if username:
            user_name = user_service.get_user_by_username(username)
            return UserSchema(many=True).dump(user_name), 200

        if admin:
            admin_u = user_service.get_by_role_admin(admin)
            return UserSchema(many=True).dump(admin_u), 200

        if user:
            user_u = user_service.get_by_role_user(user)
            return UserSchema(many=True).dump(user_u), 200

        all_users = user_service.get_all()
        res = UserSchema(many=True).dump(all_users)
        return res, 200

    def post(self):
        """Метод создания пользователя."""
        req_json = request.json
        user_service.create_user(req_json)
        return "", 201


"""Представления сущности пользователи /users/<int:bid>."""
@user_ns.route('/<int:bid>')
class UserView(Resource):
    def get(self, uid):
        """Метод получения инфы о пользователе по id."""
        try:
            user = user_service.get_one(uid)
            result = UserSchema().dump(user)
            return result, 200
        except Exception as ex:
            return ex, 404

    @auth_required
    @admin_required
    def put(self, uid):
        """Метод изменения инфы о пользователе по id"""
        req_json = request.json
        if "id" not in req_json:
            req_json["id"] = uid
        user_service.update(req_json)
        return "", 204

    @auth_required
    @admin_required
    def delete(self, uid):
        """Метод для удаления одного пользователя по его ID."""
        user_service.delete(uid)
        return "", 204
