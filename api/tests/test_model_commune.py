# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test.testcases import TransactionTestCase

from ..models import Commune


class TestModelCommune(TransactionTestCase):

    fixtures = ['regions.json', 'provinces.json', 'communes.json']

    def test_model_commune_unicode(self):
        expected = Commune.objects.get(pk=1)
        self.assertEquals(
            'Región Metropolitana - Santiago - Santiago',
            unicode(expected)
        )
