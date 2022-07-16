from dao.director import DirectorDAO


class DirectorService:
    """Класс бизнес-логики: режиссеры."""
    def __init__(self, dao: DirectorDAO):
        self.dao = dao

    def get_one(self, did):
        """Метод получения инфы о режиссере по id."""
        return self.dao.get_one(did)

    def get_all(self):
        """Метод получения инфы о всех режиссерах."""
        return self.dao.get_all()

    def create(self, director_data):
        """Метод создания нового режиссера."""
        return self.dao.create(director_data)

    def update(self, director_data):
        """Метод обновления инфы о режиссере."""
        self.dao.update(director_data)
        return self.dao

    def delete(self, did):
        """Метод удаления режиссера по id."""
        self.dao.delete(did)
