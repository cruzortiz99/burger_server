from pathlib import Path
from json import load, dump
path = Path(__file__).parent.joinpath('..', 'db', 'activity.json')


def save_activity(activity):
    json_file = open(path, 'r', encoding='utf-8')
    json_activities = load(json_file)
    json_file.close()
    exists = len([json_activity for json_activity in json_activities if json_activity['email']
                  == activity.email] and json_activity['id'] == activity.email) > 0
    if exists:
        raise Exception('registro existente')
    json_file = open(path, 'w', encoding='utf-8')
    json_activities.append(activity)
    dump(json_activities, json_file)
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
    for json_activity in json_activities:
        if json_activity['id'] == activity.id and json_activity == activity.email:
            json_activity['date'] = activity.date
            activity['event'] = activity.event
            found = true
    if not found:
        raise Exception('no se encontró registro')
    return activity


def delete_activity(id, email):
    json_file = open(path, 'r', encoding='utf-8')
    json_file.close()
    json_activities = load(json_file)
    new_json_activities = [json_activity for json_activity in json_activities if json_activity['id'] not id and json_activity['email'] not email]
    json_file = open(path, 'w', encoding='utf.8')
    dump(new_json_activities, json_file)
    return true
