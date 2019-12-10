from ..domain.repositories import activity as repository


def get_all_user_activities(email):
    return repository.get_all_activities(email)


def save_activity(activity):
    return repository.save_activity(activity)


def update_activity(activity):
    return repository.update_activity(activity)


def delete_activity(id, email):
    return repository.delete_activity(id, email)
