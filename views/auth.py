from flask import request
from flask_restx import Resource, Namespace
from implemented import auth_service

auth_ns = Namespace('auth')

"""Представления авторизации /auth/."""
@auth_ns.route('/')
class AuthView(Resource):
    def post(self):
        """Метод создания токенов авторизации."""
        req_json = request.json
        username = req_json.get('username', None)
        password = req_json.get('password', None)
        if None in [username, password]:
            return "", 400

        tokens = auth_service.generate_tokens(username, password)
        return tokens

    def put(self):
        """Метод обновления токенов авторизации."""
        req_json = request.json
        token = req_json.get('refresh_token')
        tokens = auth_service.approve_refresh_token(token)
        return tokens, 201
