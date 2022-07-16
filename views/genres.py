from flask import request
from flask_restx import Resource, Namespace
from dao.model.genre import GenreSchema
from helpers.decorators import auth_required, admin_required
from implemented import genre_service

genre_ns = Namespace('genres')

"""Представления  сущности жанры /genres/."""
@genre_ns.route('/')
class GenresView(Resource):
    @auth_required
    def get(self):
        """Метод получения инфы о всех жанрах."""
        rs = genre_service.get_all()
        res = GenreSchema(many=True).dump(rs)
        return res, 200

    @auth_required
    @admin_required
    def post(self):
        """Метод добавления нового жанра."""
        req_json = request.json
        genre = genre_service.create(req_json)
        return "", 201, {"location": f"/genres/{genre.id}"}


"""Представления сущности жанры /genres/<int:rid>."""
@genre_ns.route('/<int:rid>')
class GenreView(Resource):
    @auth_required
    def get(self, gid):
        """Метод получения жанра по его id."""
        g = genre_service.get_one(gid)
        schm_g = GenreSchema().dump(g)
        return schm_g, 200

    @auth_required
    @admin_required
    def put(self, gid):
        """Метод изменения  жанра."""
        req_json = request.json
        if "id" not in req_json:
            req_json["id"] = gid
        genre_service.update(req_json)
        return "", 204

    @auth_required
    @admin_required
    def delete(self, gid):
        """Метод удаления  жанра."""
        genre_service.delete(gid)
        return "", 204
