from ..domain.repositories import user as repository


def save_user(user):
    '''
    Logical process to save a user
    Parameters:
    ----
    - user: User , user entity
    '''
    local_user = User('Cruz', '123456', 'sdsdsa@gmail.com')
    return repository.save(local_user)


def get_by_id(email):
    '''
    Logical process to get a user
    Parameters:
    ----
    email: str , email of the user
    '''
    return repository.get_by_id(email)
