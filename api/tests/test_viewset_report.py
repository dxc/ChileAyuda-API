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
        'incidents.json',
        'styles.json',
        'categories.json',
        'media_sources.json',
        'reports.json',
    ]

    def setUp(self):
        super(TestViewSetReport, self).setUp()
        self.client = APIClient()

    def test_http_get_list(self):
        response = self.client.get('/0/incidents/{0:d}/reports/'.format(1))

        data = json.loads(response.content)

        self.assertEquals(200, response.status_code)
        self.assertEquals(1, len(data))

    def test_http_get_one(self):
        response = self.client.get('/0/incidents/{0:d}/reports/{1:d}/'.format(1, 1))

        data = json.loads(response.content)

        self.assertEquals(200, response.status_code)
        self.assertEquals(dict, type(data))

    def test_http_get_invalid(self):
        urls = [
            '/0/incidents/null/reports/',
            '/0/incidents/1/reports/null/',
        ]

        for url in urls:
            response = self.client.get(url)

            data = json.loads(response.content)

            self.assertEquals(400, response.status_code)
            self.assertEquals(1, len(data))
            self.assertIn('Invalid parameters.', data['detail'])

    def test_http_get_not_found(self):
        response = self.client.get('/0/incidents/{0:d}/reports/{1:d}/'.format(1, 999999999))

        data = json.loads(response.content)

        self.assertEquals(404, response.status_code)
        self.assertEquals(dict, type(data))
        self.assertEquals('Not found.', data['detail'])
