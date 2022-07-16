from dao.movie import MovieDAO


class MovieService:
    """Класс бизнес-логики: фильмы."""
    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def get_one(self, mid):
        """Метод получения инфы о фильме по id."""
        return self.dao.get_one(mid)

    def get_all(self, filters):
        """Метод получения инфы о всех фильмах:
        - по id режиссера ( /movies/?director_id=24 ).
        - по id жанра ( /movies/?genre_id=5 ).
        - по году выпуска (/movies/?year=2008 )."""
        if filters.get("director_id") is not None:
            movies = self.dao.get_by_director_id(filters.get("director_id"))
        elif filters.get("genre_id") is not None:
            movies = self.dao.get_by_genre_id(filters.get("genre_id"))
        elif filters.get("year") is not None:
            movies = self.dao.get_by_year(filters.get("year"))
        else:
            movies = self.dao.get_all()
        return movies

    def create(self, movie_data):
        """Метод создания нового фильма в БД."""
        return self.dao.create(movie_data)

    def update(self, movie_data):
        """Метод обновления инфы о фильме."""
        self.dao.update(movie_data)
        return self.dao

    def delete(self, mid):
        """Метод удаления фильма по id ."""
        self.dao.delete(mid)
