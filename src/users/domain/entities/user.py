class User():
    '''
    User entity model
    ----
    - name:str, name of the user

    - email:str, email and identifier of the user

    - password:str, user password
    '''

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
