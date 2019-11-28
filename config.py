class Config():
    PORT = 5000
    HOST = "localhost"


class Dev(Config):
    DEBUG = True


class Prod(Config):
    DEBUG = False
