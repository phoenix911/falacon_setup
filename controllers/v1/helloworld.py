# created by sangeet verma for project falcon_basics
# on 30/10/17 :: 1:32 AM
from falcon import HTTP_200, before
from json import dumps
from controllers.v1.validators import helloworld_validators


class HelloWorld:

    def on_get(self, req, resp):
        resp.status = HTTP_200
        resp.body = dumps({"get": "working"})

    @before(helloworld_validators.helloworld)
    def on_post(self, req,resp):
        resp.status = HTTP_200
        resp.body = dumps({"post": "working"})
