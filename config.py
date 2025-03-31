import os

class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY") or "you-will-never-guess"

    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or \
    'mysql+pymysql://root:admin@10.239.139.170:3306/microblog'

    SQLALCHEMY_TRACK_MODIFICATIONS = False
