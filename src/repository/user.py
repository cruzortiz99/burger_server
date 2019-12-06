from .entities import Entity
import json
from pathlib import Path


class User(Entity):
    def __init__(self, name, password, email):
        self.name = name
        self.password = password
        self.email = email

    def save(self):
        path = Path(__file__).parent.joinpath('..', 'db', 'user.json')
        json_file = open(path, 'r', encoding='utf-8')
        users = json.load(json_file)
        json_file.close()
        users.append(self.__dict__)
        json_file = open(path, 'w', encoding='utf-8')
        users_saved = json.dump(users, fp=json_file)
        json_file.close()
