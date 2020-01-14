from json import dump, load


def write_into_db(path, json_data):
    '''
    Write into the document on the path
    ----
    Parameters:
    ----
    - path: Path, path of the document
    - json_data: str, json format data
    Return:
    ----
    - json_data
    '''
    json_file = open(path, 'w', encoding='utf-8')
    dump(json_data, fp=json_file)
    json_file.close
    return json_data


def read_from_db(path):
    '''
    Read json data from the path
    ----
    Parameters:
    ----
    - path: Path, path to the document
    '''
    json_file = open(path, 'r', encoding='utf-8')
    json_data = load(json_file)
    json_file.close()
    return json_data
