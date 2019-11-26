class Config():
    PORT = 8000
    HOST = "localhost"


class Dev(Config):
    DEBUG = True


class Prod(Config):
    DEBUG = False
