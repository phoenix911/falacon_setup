# created by sangeet verma for project falcon_basics
# on 12/11/17 :: 3:37 AM
from falcon import HTTPUnauthorized

class AuthMiddleWare(object):

    def process_request(self, req, params):
        token = req.get_header('Authorization')
        account_key = req.get_header('Account-Key')

        if token is None:
            raise HTTPUnauthorized(
                title='Auth token required',
                description='you missed the auth token or id in header'
            )

        if not self._token_is_valid(token, account_key):
            raise HTTPUnauthorized(
                title='Invalid token',
                description='check your token'
            )

    def _token_is_valid(self, token, account_id):
        if int(token) == int(account_id):
            return True
        else:
            return False
