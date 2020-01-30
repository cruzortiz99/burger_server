from src.modules.events.domain.repositories import events as repository
from src.modules.events.domain.entities.events import Events
from re import compile
import json


def get_all_user_activities(email):
    '''
    Get all user activities as a json format
    ----
    Parameter:
    ----
    :param str email: user identifier

    Return:
    ----
    :return Tuple[json, int]: json format with the activities and
    the response status
    '''
    activities = repository.get_all_activities(email)
    return json.dumps(list(activities)), 200


def save_activity(requestBody):
    '''
    Save activity of the user process

    Parameters:
    ----
    :param {email:str, date: str, events: List[str]} requestBody:

    Return:
    ----
    :return Tuple[json, int]: with the response body and status
    '''
    try:
        activity = Events(
            email=requestBody['email'],
            messages=requestBody['messages'], date=requestBody['date'])
        activity_saved = repository.save_activity(activity)
        return json.dumps(activity_saved), 201
    except Exception:
        return {'message': "date format most be YYYY/MM/dd"}, 400


def update_activity(activity):
    activity_updated = repository.update_activity(activity)
    try:
        return json.dumps(activity_updated.__dict__), 201
    except Exception:
        return {'message': 'No event found'}


def delete_activity(id, email):
    activity_deleted = repository.delete_activity(id, email)
    return json.dumps(activity_deleted)
