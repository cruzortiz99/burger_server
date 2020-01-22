from graphene import ObjectType, String, Schema, List, Interface


class UserQuery(ObjectType):
    name = String(name=String(default_value="yo"))
    email = String()
    password = String()
    event = List(String)

    @staticmethod
    def resolve_name(parent, info, name):
        return f'Hola {name}'

    @staticmethod
    def resolve_email(parent, info):
        return f'Resolve email'

    @staticmethod
    def resolve_password(parent, info):
        return 'Resolve password'

    @staticmethod
    def resolve_event(paren, info):
        return ['Resolve event']


schema = Schema(UserQuery)
