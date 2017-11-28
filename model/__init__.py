# created by sangeet verma for project falcon_basics
# on 27/11/17 :: 1:02 AM

from mongoengine import register_connection

alias = 'core'


def global_connection():
    register_connection(
        alias=alias,
        name='setup_demo'
    )
