# created by sangeet verma for project falcon_basics
# on 12/11/17 :: 4:43 AM

from falcon import HTTPUnauthorized


def validate_user(req, resp, resource, params):
    token = req.get_header('Authorization')
    account_key = req.get_header('Account-Key')

    if token is None or account_key is None:
        raise HTTPUnauthorized(
            title='Auth token required',
            description='you missed the auth token or id in header'
        )

    if not token_is_valid(token, account_key):
        raise HTTPUnauthorized(
            title='Invalid token',
            description='check your token'
        )


def token_is_valid(token, account_key):
    """
    update this function to match your authentication logic
    :param token: user token
    :param account_key: user key
    :return: boolean ,
    True is successful validation
    """
    if int(token) == int(account_key):
        return True
    else:
        return False
