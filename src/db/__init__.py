from pathlib import Path
from json import dump
from typing import Iterator

_activities_entity: Path = Path(__file__).parent.joinpath(
    '.', 'activity.json')
_user_entity: Path = Path(__file__).parent.joinpath('.', 'user.json')


def create_db_iterable() -> Iterator:
    '''
    Create a document DB for every path
    '''
    paths = [_activities_entity, _user_entity]
    for file_path in paths:
        try:
            open(file_path, 'r').close()
            yield file_path.name
        except FileNotFoundError:
            json_file = open(file_path, 'w')
            dump([], json_file)
            json_file.close()
            yield file_path.name


def create_db():
    for entity in create_db_iterable():
        print(f'Loading database entity: {entity}')
