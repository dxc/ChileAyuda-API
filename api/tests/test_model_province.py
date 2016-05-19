# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test.testcases import TransactionTestCase

from ..models import Province


class TestModelProvince(TransactionTestCase):

    fixtures = ['regions.json', 'provinces.json']

    def test_model_province_unicode(self):
        expected = Province.objects.get(pk=131)
        self.assertEquals('Región Metropolitana - Santiago', unicode(expected))
