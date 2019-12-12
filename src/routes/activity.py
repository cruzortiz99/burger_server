from flask import request
from ..controllers import activity as controller
from ..domain.entities.activity.activity import Activities


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

    @app.route(f'{base_url}/<email>', methods=['GET'])
    def get_all_user_activities():
        return controller.get_all_user_activities('cruzortiz099@gmail.com')

    @app.route(f'{base_url}', methods=['POST'])
    def save_activity():
        request_activity = Activities(
            request.form['email'], request.form['date'], request.form['event'])
        return controller.save_activity(request_activity)

    @app.route(f'{base_url}', methods=['PUT'])
    def update_activity():
        request_activity = Activities(
            request.form['email'], request.form['date'], request.form['event'])
        return controller.update_activity(request_activity)

    @app.route(f'{base_url}/<int:id>/<email>', methods=['DELETE'])
    def delete_activity(id, email):
        return controller.delete_activity(id, email)
