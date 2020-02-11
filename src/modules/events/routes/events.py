from flask import Blueprint, request, make_response, Response
from src.modules.events.controllers import events as controller
from src.modules.events.domain.entities.events import Events
from src.utils.cors import add_cors_to_response, cors_preflight_response
import json

router = Blueprint('events', __name__)


@router.route('/<email>', methods=['GET', 'OPTIONS'])
def get_all_user_activities(email: str) -> Response:
    '''
    Get all users activities
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
def save_activity() -> Response:
    '''
    Save one activity of the user
    '''
    if request.method.upper() == 'options'.upper():
        return cors_preflight_response()
    requestBody = json.loads(request.data)
    controller_response = controller.save_activity(requestBody)
    response = make_response(controller_response[0], controller_response[1])
    response.headers['Content-Type'] = 'application/json'
    return add_cors_to_response(response)


@router.route('', methods=['PUT', 'OPTIONS'])
def update_activity() -> Response:
    '''
    Updates an existing event
    '''
    if request.method.upper() == 'options'.upper():
        return cors_preflight_response()
    request_body = json.loads(request.data)
    controller_response = controller.update_activity(request_body)
    response = make_response(controller_response[0], controller_response[1])
    response.headers['Content-Type'] = 'application/json'
    return add_cors_to_response(response)


@router.route('', methods=['PATCH', 'OPTIONS'])
def delete_activity() -> Response:
    '''
    Deletes an existing event
    '''
    if request.method.upper() == 'options'.upper():
        return cors_preflight_response()
    request_body = json.loads(request.data)
    controller_response = controller.delete_activity(
        request_body['email'],
        request_body['date'])
    response = make_response(controller_response[0], controller_response[1])
    response.headers['Content-Type'] = 'application/json'
    return add_cors_to_response(response)
