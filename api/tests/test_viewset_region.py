# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

from django.test.testcases import TransactionTestCase
from rest_framework.test import APIClient


class TestViewSetRegion(TransactionTestCase):

    fixtures = ['regions.json']

    def setUp(self):
        super(TestViewSetRegion, self).setUp()
        self.client = APIClient()

    def test_http_get(self):
        response = self.client.get('/0/regions/')

        self.assertEquals(200, response.status_code)
        self.assertEquals(1, len(json.loads(response.content)))
