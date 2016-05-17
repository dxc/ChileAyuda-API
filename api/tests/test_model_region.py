# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test.testcases import TransactionTestCase

from ..models import Region


class TestModelRegion(TransactionTestCase):

    fixtures = ['regions.json']

    def test_model_region_order(self):
        properties = {
            'id': 10,
            'name': 'Región de los Lagos',
        }

        expected = Region(**properties)
        expected.save()

        surveys = Region.objects.all()
        self.assertEquals(2, len(surveys))
        self.assertEquals(expected, surveys[0])

    def test_model_region_unicode(self):
        expected = Region.objects.get(pk=13)
        self.assertEquals('13 - Región Metropolitana', unicode(expected))
