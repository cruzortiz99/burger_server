from pathlib import Path
from json import load, dump
from src.utils.repositories import read_from_db, write_into_db
from src.modules.events.domain.entities.events import Events

path = Path(__file__).parent.joinpath(
    '..', '..', '..', '..', 'db', 'activity.json')


def save_activity(activity):
    '''
    Save the activity in the bd

    Parameters:
    ----
    :param Event activity: data model

    Return:
    ----
    :return json: activities saved in bd
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
                event_of_the_day['messages'] = activity.messages
    else:
        json_activities.append(activity.__dict__)
    return write_into_db(path, json_activities)


def get_all_activities(email):
    '''
    Get all activities associated with the user

    Parameters:
    ----
    :param str email: user identifier

    Return:
    ----
    :return generator: generator with the activities
    '''
    json_activities = read_from_db(path)
    return (json_activity for json_activity in json_activities
            if json_activity['email'] == email)


def update_activity(activity):
    '''
    Update an activity

    Parameters:
    ----
    :param Event activity: data to update

    Return:
    ----
    :return json: json with activities
    '''
    json_file = open(path, 'r', encoding='utf-8')
    json_activities = load(json_file)
    found = False
    for json_activity in json_activities:
        same_date = json_activity['date'] == activity.date
        same_email = json_activity['email'] == activity.email
        if same_date and same_email:
            json_activity['messages'] = activity.messages
            found = True
    if not found:
        raise Exception('no se encontró registro')
    return write_into_db(path, json_activities)


def delete_activity(email, date):
    '''
    Delete an event

    Parameters:
    ----
    :param str email: email of the user

    :param str date: date of the event

    Return:
    ----
    :return json: json with activities
    '''
    json_file = open(path, 'r', encoding='utf-8')
    json_activities = load(json_file)
    json_file.close()
    new_json_activities = [json_activity for json_activity in json_activities
                           if json_activity['email']
                           != email or json_activity['date'] != date]
    write_into_db(path, new_json_activities)
    return new_json_activities
