from flask import Blueprint, request, make_response
from src.modules.events.controllers import events as controller
from src.modules.events.domain.entities.events import Events
from src.utils.cors import add_cors_to_response, cors_preflight_response
import json

router = Blueprint('events', __name__)


@router.route('/<email>', methods=['GET', 'OPTIONS'])
def get_all_user_activities(email):
    '''
    Get all users activities
    ----
    Parameters:
    ----
    - email: str, user identifier
    Return:
    ----
    - response object
    '''
    if request.method.upper() == 'OPTIONS'.upper():
        return cors_preflight_response()
    controller_response = controller.get_all_user_activities(
        email)
    response = make_response(
        controller_response[0], controller_response[1])
    response.headers['Content-Type'] = 'application/json'
    return add_cors_to_response(response)


@router.route('', methods=['POST', 'OPTIONS'])
def save_activity():
    '''
    Save one activity of the user

    Return:
    ----
    - response object
    '''
    if request.method.upper() == 'options'.upper():
        return cors_preflight_response()
    requestBody = json.loads(request.data)
    response = make_response(controller.save_activity(requestBody))
    response.headers['Content-Type'] = 'application/json'
    return add_cors_to_response(response)


@router.route('/<int:id>', methods=['PUT'])
def update_activity(id):
    json_request = json.loads(request.data)
    request_activity = Events(
        email=json_request['email'], date=json_request['date'],
        events=json_request['events'])
    request_activity.id = id
    response = make_response(controller.update_activity(request_activity))
    response.headers['Content-Type'] = 'application/json'
    return response


@router.route('/<int:id>', methods=['DELETE'])
def delete_activity(id):
    email = request.headers['token']
    response = make_response(controller.delete_activity(id, email))
    response.headers['Content-Type'] = 'application/json'
    return response
