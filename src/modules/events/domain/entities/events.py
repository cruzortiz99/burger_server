import datetime
from re import compile


class Events():
    '''
    Activity model
    ----
    - email: str, user email
    - event: List[str], event message list
    - date: str, of the date time format YYYY/MM/dd
    '''

    def __init__(self, email, messages=[], date=datetime.datetime.now()
                 .strftime('%Y/%m/%d')):
        if len(date) == 0 or compile(
                r'^(\d){4}\/(\d){2}\/(\d){2}$').match(date) is None:
            raise Exception('date must be in format YYYY/MM/dd')
        self.date = date
        self.email = email
        self.messages = messages
