from pathlib import Path
from json import load, dump
from src.utils.repositories import read_from_db, write_into_db

path = Path(__file__).parent.joinpath(
    '..', '..', '..', '..', 'db', 'activity.json')


def save_activity(activity):
    '''
    Save the activity in the bd
    ----
    Parameters:
    - activity: Activity, data model
    Return:
    ----
    - Activity saved
    '''
    json_file = open(path, 'r', encoding='utf-8')
    json_activities = load(json_file)
    json_file.close()
    exists = len([json_activity for json_activity in json_activities
                  if json_activity['email'] == activity.email
                  and json_activity['date'] == activity.date]) > 0
    if exists:
        for event_of_the_day in json_activities:
            same_email = event_of_the_day['email'] == activity.email
            same_date = event_of_the_day['date'] == activity.date
            if same_email and same_date:
                event_of_the_day = activity.__dict__
    else:
        json_activities.append(activity.__dict__)
    return write_into_db(path, json_activities)


def get_all_activities(email):
    '''
    Get all activities associated with the user
    ----
    Parameter:
    ----
    - email: str, user identifier
    Return:
    ----
    - generator with the activities
    '''
    json_activities = read_from_db(path)
    return (json_activity for json_activity in json_activities
            if json_activity['email'] == email)


def update_activity(activity):
    json_file = open(path, 'r', encoding='utf-8')
    json_activities = load(json_file)
    found = False
    print(activity.__dict__)
    for json_activity in json_activities:
        same_id = json_activity['id'] == activity.id
        same_email = json_activity['email'] == activity.email
        if same_id and same_email:
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
    new_json_activities = [json_activity for json_activity in json_activities
                           if json_activity['id']
                           != ident or json_activity['email'] != email]
    json_file = open(path, 'w', encoding='utf-8')
    dump(new_json_activities, fp=json_file)
    json_file.close()
    return [json_activity for json_activity in json_activities
            if json_activity['id'] == ident
            and json_activity['email'] == email]
