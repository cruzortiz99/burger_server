from flask import make_response, Response


def cors_preflight_response() -> Response:
    '''
    Make an empty cors header to the response
    '''
    response: Response = make_response()
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = '*'
    response.headers['Access-Control-Allow-Methods'] = '*'
    return response


def add_cors_to_response(response: Response) -> Response:
    '''
    Add cors headers to the response
    '''
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response
