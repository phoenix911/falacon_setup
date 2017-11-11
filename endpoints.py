# created by sangeet verma for project falcon_basics
# on 30/10/17 :: 1:26 AM

from falcon import API
from controllers.v1 import helloworld
import authentication

api = API(
    middleware=[authentication.AuthMiddleWare()]
)
api.add_route('/hello', helloworld.HelloWorld())
