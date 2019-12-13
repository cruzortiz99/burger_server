from pathlib import Path
import json

_activities_entity = Path(__file__).parent.joinpath(
    '..', 'db', 'activity.json')
_user_entity = Path(__file__).parent.joinpath('..', 'db', 'user.json')


def create_db_iterable():
    paths = [_activities_entity, _user_entity]
    for file_path in paths:
        try:
            open(file_path, 'r').close()
            yield file_path.name
        except FileNotFoundError:
            json_file = open(file_path, 'w')
            json.dump([], json_file)
            json_file.close()
            yield file_path.name


def create_db():
    for entity in create_db_iterable():
        print(f'Loading database entity: {entity}')
