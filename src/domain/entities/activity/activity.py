import datetime


class Activities():
    _id = 0

    def __init__(self, email, event, date=datetime.datetime.now):
        Activities._id += 1
        self.id = Activities._id
        self.email = email
        self.date = date
        self.event = event
