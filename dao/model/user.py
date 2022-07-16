from setup_db import db
from marshmallow import Schema, fields


class User(db.Model):
	__tablename__ = 'user'
	"""Модель для пользователя."""
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String)
	password = db.Column(db.String)
	role = db.Column(db.String(30))


class UserSchema(Schema):
	"""Схема для сериализации пользователей."""
	id = fields.Int()
	username = fields.Str()
	password = fields.Str()
	role = fields.Str()
