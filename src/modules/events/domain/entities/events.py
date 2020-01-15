import datetime


class Events():
    '''
    Activity model
    ----
    - email: str, user email
    - event: List[str], event message list
    - date: str, of the date time format YYYY-MM-dd
    '''

    def __init__(self, email, events=[], date=datetime.datetime.now()
                 .strftime('%Y-%m-%d')):
        self.email = email
        self.date = date
        self.events = events
