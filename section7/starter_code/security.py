from werkzeug.security import safe_str_cmp
from models.user import UserModel

def authenticate(username, password):
    """
    Function that gets called when user /auth calls /auth endpoint.
    :param username:  User's username
    :param password: unencrypted password
    :return: UserModel object if authenticated and None otherwise
    """

    user = UserModel.find_by_username(username)
    if user and safe_str_cmp(user.password, password):
        return user

def identity(payload):
    """
    Function that gets called when user has already authenticated, and Flask-JWT
    verified their authorization header is
    :param payload: dictionary with 'identity' key
    :return:
    """
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)