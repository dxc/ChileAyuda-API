# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

from django.test.testcases import TransactionTestCase
from rest_framework.test import APIClient


class TestViewProvinceSet(TransactionTestCase):

    fixtures = ['regions.json', 'provinces.json', 'communes.json']

    def setUp(self):
        super(TestViewProvinceSet, self).setUp()
        self.client = APIClient()

    def test_http_get(self):
        response = self.client.get('/0/communes/?province={0:d}'.format(1))

        self.assertEquals(200, response.status_code)
        self.assertEquals(1, len(json.loads(response.content)))

    def test_http_get_no_invalid(self):
        params_list = [
            '',
            '?province=',
            '?province=null',
            '?province=999999'
        ]

        for params in params_list:
            response = self.client.get('/0/communes/' + params)

            self.assertEquals(200, response.status_code)
            self.assertEquals(0, len(json.loads(response.content)))
