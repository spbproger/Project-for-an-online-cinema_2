from dao.genre import GenreDAO


class GenreService:
    """Класс бизнес-логики: жанры."""
    def __init__(self, dao: GenreDAO):
        self.dao = dao

    def get_one(self, gid):
        """Метод получения инфы о жанре по id."""
        return self.dao.get_one(gid)

    def get_all(self):
        """Метод получения инфы о всех жанрах."""
        return self.dao.get_all()

    def create(self, genre_data):
        """Метод создания нового жанра."""
        return self.dao.create(genre_data)

    def update(self, genre_data):
        """Метод обновления жанра."""
        self.dao.update(genre_data)
        return self.dao

    def delete(self, gid):
        """Метод удаления жанра."""
        self.dao.delete(gid)
