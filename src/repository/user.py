from repository.entities import Entity


class User(Entity):
    def __init__(self, name, password):
        self.name = name
        self.password = password
