# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

from django.test.testcases import TransactionTestCase
from rest_framework.test import APIClient


class TestViewSetUser(TransactionTestCase):

    fixtures = [
        'users.json',
    ]

    def setUp(self):
        super(TestViewSetUser, self).setUp()
        self.client = APIClient()

    def test_http_get(self):
        response = self.client.get(
            '/0/users/{0:d}/'.format(1)
        )

        expected = json.loads(response.content)

        self.assertEquals(200, response.status_code)
        self.assertEquals(dict, type(expected))
        self.assertEquals(1, expected['id'])

    def test_http_get_invalid(self):
        urls = [
            '/0/users/null/',
        ]

        for url in urls:
            response = self.client.get(url)

            data = json.loads(response.content)

            self.assertEquals(400, response.status_code)
            self.assertEquals(1, len(data))
            self.assertIn('User integer id required.', data)

    def test_http_get_not_found(self):
        response = self.client.get('/0/users/999999999/')

        data = json.loads(response.content)

        self.assertEquals(404, response.status_code)
        self.assertEquals(1, len(data))
        self.assertEquals('Not found.', data['detail'])
