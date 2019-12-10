from flask import request


def activities_routes(app):
    '''
    Activities routes
    - get:/activity
    - post:/activity
    - put:/activity
    - delete:/activity

    Parameters:
    ----
    - app: Flask object
    '''
    base_url = '/activity'

    @app.route(f'{base_url}', methods=['GET'])
    def get_all_user_activities():
        raise Exception('method must be implemented')

    @app.route(f'{base_url}', methods=['POST'])
    def save_activity():
        raise Exception('method must be implemented')

    @app.route(f'{base_url}', methods=['PUT'])
    def update_activity():
        raise Exception('method must be implemented')

    @app.route(f'{base_url}', methods=['DELETE'])
    def delete_activity():
        raise Exception('method must be implemented')
