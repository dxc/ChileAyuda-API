# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

from django.test.testcases import TransactionTestCase
from rest_framework.test import APIClient


class TestViewSetCategory(TransactionTestCase):

    fixtures = ['styles.json', 'categories.json']

    def setUp(self):
        super(TestViewSetCategory, self).setUp()
        self.client = APIClient()

    def test_http_get(self):
        response = self.client.get('/0/categories/')

        data = json.loads(response.content)

        self.assertEquals(200, response.status_code)
        self.assertEquals(3, len(data))
        self.assertEquals(
            {'color': '#FF0000', 'name': 'Emergencia'},
            data[0]['style']
        )
