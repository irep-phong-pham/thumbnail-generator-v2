"""
Refs: https://marshmallow.readthedocs.io/en/stable/
"""

from marshmallow import Schema, post_load
import humps


class BaseRequestSchema(Schema):
    def custom_post_load(self, data, **kwargs):
        return data

    @post_load
    def convert_to_snake_case(self, data, **kwargs):
        return humps.decamelize(self.custom_post_load(data, **kwargs))
