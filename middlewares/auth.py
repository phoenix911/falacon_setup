# created by sangeet verma for project falcon_basics
# on 12/11/17 :: 3:37 AM
from falcon import HTTPUnauthorized
from hooks.auth import token_is_valid


class AuthMiddleWare(object):

    def process_request(self, req, params):
        token = req.get_header('Authorization')
        account_key = req.get_header('Account-Key')

        if token is None:
            raise HTTPUnauthorized(
                title='Auth token required',
                description='you missed the auth token or id in header'
            )

        if not token_is_valid(token, account_key):
            raise HTTPUnauthorized(
                title='Invalid token',
                description='check your token'
            )