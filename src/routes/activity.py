from flask import request, make_response
from ..controllers import activity as controller
from ..domain.entities.activity.activity import Activities
import json


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
        email = request.headers['token']
        activities = controller.get_all_user_activities(
            email)
        response = make_response(activities)
        response.headers['Content-Type'] = 'application/json'
        return response

    @app.route(f'{base_url}', methods=['POST'])
    def save_activity():
        json_request = json.loads(request.data)
        request_activity = Activities(
            email=json_request['email'], date=json_request['date'], event=json_request['event'])
        response = make_response(controller.save_activity(request_activity))
        response.headers['Content-Type'] = 'application/json'
        return response

    @app.route(f'{base_url}/<int:id>', methods=['PUT'])
    def update_activity(id):
        json_request = json.loads(request.data)
        request_activity = Activities(
            email=json_request['email'], date=json_request['date'], event=json_request['event'])
        request_activity.id = id
        response = make_response(controller.update_activity(request_activity))
        response.headers['Content-Type'] = 'application/json'
        return response

    @app.route(f'{base_url}/<int:id>', methods=['DELETE'])
    def delete_activity(id):
        email = request.headers['token']
        response = make_response(controller.delete_activity(id, email))
        response.headers['Content-Type'] = 'application/json'
        return response
