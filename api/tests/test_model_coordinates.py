# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test.testcases import TransactionTestCase

from ..models import Coordinates


class TestModelCoordinates(TransactionTestCase):

    fixtures = ['coordinates.json']

    def test_model_coordinates_unicode(self):
        expected = Coordinates.objects.get(pk=1)
        self.assertEquals(
            '-33.4583573, -70.6631088',
            unicode(expected)
        )
