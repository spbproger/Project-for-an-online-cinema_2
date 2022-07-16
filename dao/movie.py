from dao.model.movie import Movie


# CRUD - это операции создания, чтения, обновления и удаления.
class MovieDAO:
    """ДАО для модели фильма."""
    def __init__(self, session):
        self.session = session

    def get_one(self, mid):
        """Метод получения инфы о фильме по id."""
        return self.session.query(Movie).get(mid)

    def get_all(self):
        """Метод получения инфы о всех фильмах."""
        return self.session.query(Movie).all()

    def get_by_director_id(self, did):
        """Метод получения инфы о фильмах по id режиссера (запрос:  /movies/?director_id=24 )."""
        return self.session.query(Movie).filter(Movie.director_id == did).all()

    def get_by_genre_id(self, gid):
        """Метод получения инфы о фильмах по id жанра (запрос:   /movies/?genre_id=5 )."""
        return self.session.query(Movie).filter(Movie.genre_id == gid).all()

    def get_by_year(self, year_num):
        """Метод получения инфы о фильмах по номеру года (запрос: /movies/?year=2008 )."""
        return self.session.query(Movie).filter(Movie.year == year_num).all()

    def create(self, movie_data):
        """Метод создания нового фильма."""
        movie_new = Movie(**movie_data)
        self.session.add(movie_new)
        self.session.commit()
        return movie_new

    def delete(self, mid):
        """Метод для удаления одного фильма."""
        movie = self.get_one(mid)
        self.session.delete(movie)
        self.session.commit()

    def update(self, movie_data):
        """Метод для обновления одного фильма."""
        movie = self.get_one(movie_data.get("id"))
        movie.title = movie_data.get("title")
        movie.description = movie_data.get("description")
        movie.trailer = movie_data.get("trailer")
        movie.year = movie_data.get("year")
        movie.rating = movie_data.get("rating")
        movie.genre_id = movie_data.get("genre_id")
        movie.director_id = movie_data.get("director_id")
        self.session.add(movie)
        self.session.commit()