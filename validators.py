# -*- coding: utf-8 -*-
from marshmallow import Schema, fields
from marshmallow import validate, ValidationError


class CreateRegisterSchema(Schema):

    nombres     = fields.Str(required=True, validate=validate.Length(min=1, max=200))
    apellidos   = fields.Str(required=True, validate=validate.Length(min=1, max=200))
    password    = fields.Str(required=True, validate=validate.Length(min=8, max=100))
    email       = fields.Str(required=True, validate=validate.Email())
    cedula      = fields.Str(required=True, validate=validate.Length(min=7, max=50))
    
class CreateLoginSchema(Schema):

    password   = fields.Str(required=True, validate=validate.Length(min=8, max=100))
    email      = fields.Str(required=True, validate=validate.Email())




