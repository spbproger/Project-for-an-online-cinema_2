from setup_db import db
from marshmallow import Schema, fields


class Genre(db.Model):
    __tablename__ = 'genre'
    """Модель для жанра"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))


class GenreSchema(Schema):
    """Схема для сериализации жанров."""
    id = fields.Int()
    name = fields.Str()
