from json import dump, load
from pathlib import Path


def write_into_db(path: Path, json_data: dict) -> dict:
    '''
    Write into the document on the path
    '''
    json_file = open(path, 'w', encoding='utf-8')
    dump(json_data, fp=json_file)
    json_file.close
    return json_data


def read_from_db(path: Path) -> dict:
    '''
    Read json data from the path
    '''
    json_file = open(path, 'r', encoding='utf-8')
    json_data = load(json_file)
    json_file.close()
    return json_data
