# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

from django.test.testcases import TransactionTestCase
from rest_framework.test import APIClient


class TestViewSetReportComments(TransactionTestCase):

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
        'reports_comments.json'
    ]

    def setUp(self):
        super(TestViewSetReportComments, self).setUp()
        self.client = APIClient()

    def test_http_get(self):
        response = self.client.get(
            '/0/reports/{0:d}/comments/'.format(1)
        )

        self.assertEquals(200, response.status_code)
        self.assertEquals(1, len(json.loads(response.content)))

    def test_http_get_invalid(self):
        urls = [
            '/0/reports/null/comments/',
        ]

        for url in urls:
            response = self.client.get(url)

            data = json.loads(response.content)

            self.assertEquals(400, response.status_code)
            self.assertEquals(1, len(data))
            self.assertIn('Report integer id required.', data)

    def test_http_get_not_found(self):
        response = self.client.get('/0/reports/999999999/comments/')

        data = json.loads(response.content)

        self.assertEquals(404, response.status_code)
        self.assertEquals(1, len(data))
        self.assertEquals('Report does not exist.', data['detail'])
