# created by sangeet verma for project falcon_basics
# on 30/10/17 :: 1:26 AM

from falcon import API
from middlewares import auth
from controllers.v1 import helloworld

api = API(
    # middleware=[auth.AuthMiddleWare()]
)
api.add_route('/hello', helloworld.HelloWorld())
