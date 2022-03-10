# -*- coding: utf-8 -*-
from marshmallow import Schema, fields
from marshmallow import validate, ValidationError


class CreateRegisterSchema(Schema):


    email = fields.Str(required=True, validate=validate.Email())
    password = fields.Str(required=True, validate=validate.Length(min=1, max=60))
    nombre = fields.Str(required=True, validate=validate.Length(min=1, max=60))
