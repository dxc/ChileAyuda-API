# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

from django.contrib.auth.models import User
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
        user = User.objects.get(pk=1)
        self.client.force_login(user)

        response = self.client.get('/0/sessions/')

        expected = json.loads(response.content)

        self.assertEquals(200, response.status_code)
        self.assertEquals(1, len(expected))
        self.assertEquals(1, expected[0]['id'])

        self.client.logout()

    def test_http_get_not_logged_in(self):
        response = self.client.get('/0/sessions/')

        expected = json.loads(response.content)

        self.assertEquals(200, response.status_code)
        self.assertEquals(0, len(expected))
