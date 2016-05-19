# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

from django.test.testcases import TransactionTestCase
from rest_framework.test import APIClient


class TestViewSetReport(TransactionTestCase):

    fixtures = [
        'users.json',
        'regions.json',
        'provinces.json',
        'communes.json',
        'coordinates.json',
        'disasters.json',
        'styles.json',
        'categories.json',
        'media_sources.json',
        'reports.json',
    ]

    def setUp(self):
        super(TestViewSetReport, self).setUp()
        self.client = APIClient()

    def test_http_get(self):
        response = self.client.get('/0/reports/?disaster={0:d}'.format(1))

        data = json.loads(response.content)

        self.assertEquals(200, response.status_code)
        self.assertEquals(1, len(data))

    def test_http_get_invalid(self):
        params_list = [
            '',
            '?disaster=',
            '?disaster=null',
        ]

        for params in params_list:
            response = self.client.get('/0/reports/' + params)

            data = json.loads(response.content)

            self.assertEquals(400, response.status_code)
            self.assertEquals(1, len(data))
            self.assertIn('Disaster integer id required.', data)

    def test_http_get_not_found(self):
        response = self.client.get('/0/reports/?disaster=999999999')

        data = json.loads(response.content)

        self.assertEquals(404, response.status_code)
        self.assertEquals(1, len(data))
        self.assertEquals('Disaster does not exist.', data['detail'])
