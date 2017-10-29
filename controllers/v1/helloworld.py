# created by sangeet verma for project falcon_basics
# on 30/10/17 :: 1:32 AM
from falcon import HTTP_200
from json import dumps


class HelloWorld:

    # @falcon.before()
    def on_get(self, req, resp):
        resp.status = HTTP_200
        resp.body = dumps({"get": "working"})

    def on_post(self, req,resp):
        resp.status = HTTP_200
        resp.body = dumps({"post": "working"})

