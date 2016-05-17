# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test.testcases import TransactionTestCase

from ..models import Style


class TestModelStyle(TransactionTestCase):

    fixtures = ['styles.json']

    def test_model_style_unicode(self):
        expected = Style.objects.get(pk=1)
        self.assertEquals(
            'Emergencia',
            unicode(expected)
        )
