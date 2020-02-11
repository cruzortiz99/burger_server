from src.modules.events.domain.repositories import events as repository
from src.modules.events.domain.entities.events import Events
from re import compile
import json
from typing import Tuple, List, Union, Iterable


def get_all_user_activities(email: str) -> Tuple[str, int]:
    '''
    Get all user activities as a json format
    '''
    activities: Iterable = repository.get_all_activities(email)
    return json.dumps(list(activities)), 200


def save_activity(requestBody: dict) -> Tuple[Union[dict, str], int]:
    '''
    Save activity of the user process
    '''
    try:
        activity: Events = Events(
            email=requestBody['email'],
            messages=requestBody['messages'], date=requestBody['date'])
        activity_saved = repository.save_activity(activity)
        return json.dumps(activity_saved), 201
    except Exception:
        return {'message': "date format most be YYYY/MM/dd"}, 400


def update_activity(requestBody: dict) -> Tuple[Union[dict, str], int]:
    '''
    Logic process to update an event
    '''
    try:
        activity: Events = Events(
            email=requestBody['email'],
            messages=requestBody['messages'],
            date=requestBody['date'])
        activity_updated = repository.update_activity(activity)
        return json.dumps(activity_updated), 201
    except Exception:
        return {'message': 'No event found'}, 404


def delete_activity(email: str, date: str) -> Tuple[str, int]:
    '''
    Deletes an event
    '''
    activity_deleted = repository.delete_activity(email, date)
    return json.dumps(activity_deleted), 201
