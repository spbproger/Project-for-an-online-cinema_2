from dao.model.genre import Genre


# CRUD - это операции создания, чтения, обновления и удаления.
class GenreDAO:
    """ДАО для модели жанра."""
    def __init__(self, session):
        self.session = session

    def get_one(self, gid):
        """Метод получения инфы о жанре по id."""
        return self.session.query(Genre).get(gid)

    def get_all(self):
        """Метод получения инфы о всех жанрах."""
        return self.session.query(Genre).all()

    def create(self, genre_data):
        """Метод создания нового жанра в БД."""
        genre_new = Genre(**genre_data)
        self.session.add(genre_new)
        self.session.commit()
        return genre_new

    def delete(self, gid):
        """Метод удаления жанра по id."""
        genre = self.get_one(gid)
        self.session.delete(genre)
        self.session.commit()

    def update(self, genre_data):
        """Метод для обновления одного жанра."""
        genre = self.get_one(genre_data.get("id"))
        genre.name = genre_data.get("name")
        self.session.add(genre)
        self.session.commit()
