import jwt
import traceback
from functools import wraps
from collections import namedtuple

from flask import request
import flask_restful
from webargs import ValidationError
from webargs.flaskparser import parser

from src.controllers.common import http_exceptions
from src.exceptions import WebAPIException, ErrorCode


@parser.error_handler
def handle_error(error, req, schema, *, error_status_code, error_headers):
    raise error


class BaseController(flask_restful.Resource):
    def __init__(self, *args, **kwargs):
        super().__init__()
