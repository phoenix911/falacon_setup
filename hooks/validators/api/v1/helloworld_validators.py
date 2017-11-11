# created by sangeet verma for project falcon_basics
# on 31/10/17 :: 8:32 AM
import hooks.validators.api as v

schema = {
    'phone': {
        v.type_: v.type_int,
        v.maxLength: 10,
        v.coerce: int,
        v.required: True
    }, 'password': {
        v.type_: v.type_str,
        v.minLength: 6,
        v.required: False
    }, 'email': {
        v.validator: v.validate_email,
        v.required: True,
    }, 'validity': {
        v.validator: v.validate_bool01,
        v.required: True
    }, 'dob': {
       v.validator: v.validate_date,
       v.required: True
    }, 'tob': {
       v.validator: v.validate_time,
       v.required: True
    }, 'current': {
        v.validator: v.validate_date_time,
        v.required: True
    }
}

validator = v.Validator(schema)


def helloworld(req, resp, resource, params):
    if not validator.validate(req.params):
        raise v.bad_request(validator)
