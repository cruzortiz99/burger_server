from pathlib import Path
from json import load, dump
path = Path(__file__).parent.joinpath('..', '..', 'db', 'activity.json')


def save_activity(activity):
    json_file = open(path, 'r', encoding='utf-8')
    json_activities = load(json_file)
    json_file.close()
    exists = len([json_activity for json_activity in json_activities if json_activity['email']
                  == activity.email and json_activity['id'] == activity.id]) > 0
    if exists:
        print(activity.__dict__)
        raise Exception('registro existente')
    json_activities.append(activity.__dict__)
    print(json_activities)
    json_file = open(path, 'w', encoding='utf-8')
    dump(json_activities, fp=json_file)
    json_file.close()
    return activity


def get_all_activities(email):
    json_file = open(path, 'r', encoding='utf-8')
    json_activities = load(json_file)
    json_file.close()
    return [json_activity for json_activity in json_activities if json_activity['email'] == email]


def update_activity(activity):
    json_file = open(path, 'r', encoding='utf-8')
    json_activities = load(json_file)
    found = False
    print(activity.__dict__)
    for json_activity in json_activities:
        if json_activity['id'] == activity.id and json_activity['email'] == activity.email:
            json_activity['date'] = activity.date
            json_activity['event'] = activity.event
            found = True
    if not found:
        raise Exception('no se encontró registro')
    json_file = open(path, 'w', encoding='utf-8')
    dump(json_activities, json_file)
    json_file.close()
    return activity


def delete_activity(ident, email):
    json_file = open(path, 'r', encoding='utf-8')
    json_activities = load(json_file)
    json_file.close()
    new_json_activities = [json_activity for json_activity in json_activities if json_activity['id']
                           != ident or json_activity['email'] != email]
    json_file = open(path, 'w', encoding='utf-8')
    dump(new_json_activities, fp=json_file)
    json_file.close()
    return [json_activity for json_activity in json_activities if json_activity['id'] == ident and json_activity['email'] == email]
