# created by sangeet verma for project falcon_basics
# on 31/10/17 :: 8:32 AM
import validators.controllers as v

schema_post = {
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

schema_put = {
    'phone': {
        v.type_: v.type_int,
        v.coerce: int
    }, 'number': {
        v.validator: v.validate_date
    }
}
