from flask import request
from flask_restx import Resource, Namespace
from dao.model.director import DirectorSchema
from helpers.decorators import auth_required, admin_required
from implemented import director_service

director_ns = Namespace('directors')

"""Представления сущности режиссеры /directors/."""
@director_ns.route('/')
class DirectorsView(Resource):
    @auth_required
    def get(self):
        """Метод получения инфы о всех режиссерах."""
        rs = director_service.get_all()
        res = DirectorSchema(many=True).dump(rs)
        return res, 200

    @auth_required
    @admin_required
    def post(self):
        """Метод добавления нового режиссера."""
        req_json = request.json
        director = director_service.create(req_json)
        return "", 201, {"location": f"/directors/{director.id}"}


"""Представления сущности режиссера /directors/<int:rid>."""
@director_ns.route('/<int:rid>')
class DirectorView(Resource):
    @auth_required
    def get(self, did):
        """Метод получения инфы о режиссере по его id."""
        d = director_service.get_one(did)
        schm_d = DirectorSchema().dump(d)
        return schm_d, 200

    @auth_required
    @admin_required
    def put(self, did):
        """Метод изменения инфы о режиссере."""
        req_json = request.json
        if "id" not in req_json:
            req_json["id"] = did
        director_service.update(req_json)
        return "", 204

    @auth_required
    @admin_required
    def delete(self, did):
        """Метод удаления режиссера по id."""
        director_service.delete(did)
        return "", 204
