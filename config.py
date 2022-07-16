# Файл, в котором хранятся настройки для программы

class Config(object):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///./movies.db'               # База данных
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    RESTX_JSON = {'ensure_ascii': False, 'indent': 4}


