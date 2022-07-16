from dao.model.director import Director


# CRUD - это операции создания, чтения, обновления и удаления.
class DirectorDAO:
    """ДАО для модели директора"""
    def __init__(self, session):
        self.session = session

    def get_one(self, did):
        """Метод получения инфы о режиссере по id."""
        return self.session.query(Director).get(did)

    def get_all(self):
        """Метод получения инфы о всех режиссерах."""
        return self.session.query(Director).all()

    def create(self, director_data):
        """Метод создания нового режиссера в БД."""
        director_new = Director(**director_data)
        self.session.add(director_new)
        self.session.commit()
        return director_new

    def delete(self, did):
        """Метод удаления одного режиссера по id."""
        director = self.get_one(did)
        self.session.delete(director)
        self.session.commit()

    def update(self, director_data):
        """Метод обновления инфы о режиссере."""
        director = self.get_one(director_data.get("id"))
        director.name = director_data.get("name")
        self.session.add(director)
        self.session.commit()
