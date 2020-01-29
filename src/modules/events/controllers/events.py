from src.modules.events.domain.repositories import events as repository
from src.modules.events.domain.entities.events import Events
import json


def get_all_user_activities(email):
    '''
    Get all user activities as a json format
    ----
    Parameter:
    - email: str, user identifier
    ----
    Return:
    - tuple json format with the activities and the response status
    '''
    activities = repository.get_all_activities(email)
    return json.dumps(list(activities)), 200


def save_activity(requestBody):
    '''
    Save activity of the user process
    ----
    Parameters:
    ----
    - requestBody: {email:str, date: str, events: List[str]}
    Return:
    ----
    - tuple with the response body and status
    '''
    activity = Events(
        email=requestBody['email'], date=requestBody['date'],
        messages=requestBody['events'])
    activity_saved = repository.save_activity(activity)
    return json.dumps(activity_saved.__dict__), 200


def update_activity(activity):
    activity_updated = repository.update_activity(activity)
    return json.dumps(activity_updated.__dict__)


def delete_activity(id, email):
    activity_deleted = repository.delete_activity(id, email)
    return json.dumps(activity_deleted)
