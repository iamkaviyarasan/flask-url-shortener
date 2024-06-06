from functools import wraps

from flask import redirect, request, Response,current_app, session




def check_auth(username, password):
    """This function is called to check if a username /
    password combination is valid.
    """
    return username == current_app.config['ADMIN_USERNAME'] \
          and password == current_app.config['ADMIN_PASSWORD']


def authenticate():
    """Sends a 401 response that enables basic auth"""
    return Response(
    'Could not verify your access level for that URL.\n'
    'You have to login with proper credentials', 401,
    {'WWW-Authenticate': 'Basic realm="Login Required"'})


def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)
    return decorated


def logout():
    """Logs out the user by sending a 401 response and redirecting to the root route."""
    response = Response(
        'Logged out successfully.\n'
        'Please log in again with proper credentials', 
        401,
        {'WWW-Authenticate': 'Basic realm="Login Required"'}
    )
    response.headers['Location'] = '/'  # Redirect to the root route
    return response

# @app.route('/')
# @requires_auth
# def index():
#     return 'index'