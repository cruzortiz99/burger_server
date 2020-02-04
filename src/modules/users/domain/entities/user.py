class User():
    '''
    User entity model

    Parameters:
    ----
    :param str name: name of the user

    :param str email: email and identifier of the user

    :param str password: user password
    '''

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
