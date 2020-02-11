class Config():
    PORT: int = 5000
    HOST: str = "localhost"


class Dev(Config):
    DEBUG: bool = True


class Prod(Config):
    DEBUG: bool = False
