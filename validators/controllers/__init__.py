# created by sangeet verma for project falcon_basics
# on 31/10/17 :: 8:29 AM
from cerberus import Validator
from falcon import HTTPBadRequest
from re import compile
from datetime import datetime
from setup import date_format, time_format, date_time_format

type_ = "type"
type_int = "integer"
type_str = "string"
type_bool = "boolean"
type_date = "date"

coerce = "coerce"
maxLength = "maxlength"
minLength = "minlength"
required = "required"
validator = "validator"

regex_email = '[a-zA-Z0-9._-]+@(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,4}'


def validate_bool01(field, value, error):
    try:
        if int(value) == 0 or int(value) == 1:
            pass
        else:
            error(field, "must be 0 or 1")
    except ValueError:
        error(field, "not an integer")


def validate_email(field, value, error):
    pattern = compile(regex_email)
    if pattern.match(value):
        pass
    else:
        error(field, "not an email")


def validate_date(field, value, error):
    # pattern = compile(regex_date)
    try:
        datetime.strptime(value, date_format)
        pass
    except ValueError:
        error(field, "wrong date format")


def validate_time(field, value, error):
    try:
        datetime.strptime(value, time_format)
        pass
    except ValueError:
        error(field, "time format error")


def validate_date_time(field, value, error):
    try:
        datetime.strptime(value, date_time_format)
        pass
    except ValueError:
        error(field, "date time format error")


def bad_request(validator_):
    return HTTPBadRequest(title="unaddressable request", description=validator_.errors)


def validate_params(schema):
    validator__ = Validator(schema)

    def validate_schema(req, resp, resource, params):
        if not validator__.validate(req.params):
            raise bad_request(validator__)

    return validate_schema

