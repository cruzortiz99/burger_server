import datetime
from re import compile
from typing import List


class Events():
    '''
    Event model
    '''

    def __init__(
            self,
            email: str,
            messages: List[dict] = [],
            date: str = datetime.datetime.now().strftime('%Y/%m/%d')):
        if len(date) == 0 or compile(
                r'^(\d){4}\/(\d){2}\/(\d){2}$').match(date) is None:
            raise Exception('date must be in format YYYY/MM/dd')
        self.date = date
        self.email = email
        self.messages = messages
