# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

from django.test.testcases import TransactionTestCase
from rest_framework.test import APIClient


class TestViewSetCommune(TransactionTestCase):

    fixtures = ['regions.json', 'provinces.json', 'communes.json']

    def setUp(self):
        super(TestViewSetCommune, self).setUp()
        self.client = APIClient()

    def test_http_get(self):
        response = self.client.get('/0/communes/?province={0:d}'.format(131))

        self.assertEquals(200, response.status_code)
        self.assertEquals(1, len(json.loads(response.content)))

    def test_http_get_invalid(self):
        params_list = [
            '',
            '?province=',
            '?province=null',
        ]

        for params in params_list:
            response = self.client.get('/0/communes/' + params)

            data = json.loads(response.content)

            self.assertEquals(400, response.status_code)
            self.assertEquals(1, len(data))
            self.assertIn('Province integer id required.', data)

    def test_http_get_not_found(self):
        response = self.client.get('/0/communes/?province=999999999')

        data = json.loads(response.content)

        self.assertEquals(404, response.status_code)
        self.assertEquals(1, len(data))
        self.assertEquals('Province does not exist.', data['detail'])
