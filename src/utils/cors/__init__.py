from flask import make_response


def cors_preflight_response():
    '''
    Make an empty cors header to the response
    ----
    Return:

    - response
    '''
    response = make_response()
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = '*'
    response.headers['Access-Control-Allow-Methods'] = '*'
    return response


def add_cors_to_response(response):
    '''
    Add cors headers to the response

    Return
    ----
    - response
    '''
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response
