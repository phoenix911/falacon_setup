# created by sangeet verma for project falcon_basics
# on 30/10/17 :: 1:32 AM
from json import dumps

from falcon import HTTP_200, before
from validators.controllers import validate_params

from hooks.auth import validate_user
from validators.controllers.v1.helloworld import schema


class HelloWorld:

    @before(validate_user)
    def on_get(self, req, resp):
        resp.status = HTTP_200
        resp.body = dumps({"get": "working"})

    # @before(validate_user)
    @before(validate_params(schema))
    def on_post(self, req, resp):
        resp.status = HTTP_200
        resp.body = dumps({"post": "working"})
