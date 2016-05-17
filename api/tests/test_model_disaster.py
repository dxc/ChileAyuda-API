# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test.testcases import TransactionTestCase

from ..models import Disaster


class TestModelDisaster(TransactionTestCase):

    fixtures = [
        'regions.json',
        'provinces.json',
        'communes.json',
        'coordinates.json',
        'users.json',
        'disasters.json'
    ]

    def test_model_disaster_unicode(self):
        expected = Disaster.objects.get(pk=1)
        self.assertEquals(
            'Desastre de prueba en Beauchef',
            unicode(expected)
        )
