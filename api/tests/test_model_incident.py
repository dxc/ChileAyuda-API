# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test.testcases import TransactionTestCase

from ..models import Incident


class TestModelIncident(TransactionTestCase):

    fixtures = [
        'regions.json',
        'provinces.json',
        'communes.json',
        'coordinates.json',
        'users.json',
        'incidents.json'
    ]

    def test_model_incident_unicode(self):
        expected = Incident.objects.get(pk=1)
        self.assertEquals(
            'Incidente de prueba en Beauchef',
            unicode(expected)
        )
