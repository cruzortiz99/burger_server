from ..domain.repositories import activity as repository
import json


def get_all_user_activities(email):
    activities = repository.get_all_activities(email)
    return json.dumps(activities)


def save_activity(activity):
    activity_saved = repository.save_activity(activity)
    return json.dumps(activity_saved.__dict__)


def update_activity(activity):
    activity_updated = repository.update_activity(activity)
    return json.dumps(activity_updated.__dict__)


def delete_activity(id, email):
    activity_deleted = repository.delete_activity(id, email)
    return json.dumps(activity_deleted)
