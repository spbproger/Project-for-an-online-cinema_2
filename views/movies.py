from flask import request
from flask_restx import Resource, Namespace
from dao.model.movie import MovieSchema
from helpers.decorators import auth_required, admin_required
from implemented import movie_service

movie_ns = Namespace('movies')

"""Представления сущности фильмы /movies/."""
@movie_ns.route('/')
class MoviesView(Resource):
    @auth_required
    def get(self):
        """Метод получения инфы о всех фильмах.
        - по id режиссеров.
        - по id жанров.
        - по году выхода."""
        director = request.args.get("director_id")
        genre = request.args.get("genre_id")
        year = request.args.get("year")
        filters = {
            "director_id": director,
            "genre_id": genre,
            "year": year,
        }
        all_movies = movie_service.get_all(filters)
        res = MovieSchema(many=True).dump(all_movies)
        return res, 200

    @auth_required
    @admin_required
    def post(self):
        """Метод добавления нового фильма."""
        req_json = request.json
        movie = movie_service.create(req_json)
        return "", 201, {"location": f"/movies/{movie.id}"}


"""Представления  сущности фильмы /movies/<int:bid>."""
@movie_ns.route('/<int:bid>')
class MovieView(Resource):
    @auth_required
    def get(self, mid):
        """Метод получения инфы о фильме по id."""
        m = movie_service.get_one(mid)
        schm_m = MovieSchema().dump(m)
        return schm_m, 200

    @auth_required
    @admin_required
    def put(self, mid):
        """Метод изменения фильма по id."""
        req_json = request.json
        if "id" not in req_json:
            req_json["id"] = mid
        movie_service.update(req_json)
        return "", 204

    @auth_required
    @admin_required
    def delete(self, mid):
        """Метод удаления фильма по id."""
        movie_service.delete(mid)
        return "", 204
