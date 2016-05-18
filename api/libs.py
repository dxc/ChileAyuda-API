# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import re

from rest_framework.exceptions import APIException


class ObjectNotFound(APIException):
    status_code = 404

    def __init__(self, model):
        self.detail = '{0:s} does not exist.'.format(model)


def is_integer(value):
    if value is None:
        return False
    return re.match(r'[0-9]+', unicode(value)) is not None
